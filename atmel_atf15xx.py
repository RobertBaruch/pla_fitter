import json
import os
import pprint
import sys
import textwrap

from typing import List, Dict, Tuple, Optional


from munkres import Munkres, make_cost_matrix, DISALLOWED
from pyosys import libyosys as ys
from bitarray import bitarray
from nmigen.build import Platform, Resource, Pins, Attrs
from nmigen.build.run import BuildPlan
from nmigen.back import rtlil

from pass_register import *


# !!!!!!!!!!!!!!!!!!!!!NOTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# You must have bitarray, munkres, and nmigen installed via pip3, and also you must
# have checked out the prjbureau repo (https://github.com/whitequark/prjbureau)
# and added the repo to your PYTHONPATH.

# prjbureau stuff:
from util.fuseconv import read_jed, write_jed
from util.fusecli import FuseTool, parse_filters

ID_ATTR_IO_FUNC = ys.IdString("$io_func")
ID_PORT_A = ys.IdString("\\A")
ID_PORT_E = ys.IdString("\\E")
ID_PORT_Y = ys.IdString("\\Y")
ID_PORT_PAD = ys.IdString("\\PAD")
ID_PORT_IO_A = ys.IdString("\\IO.A")
ID_PORT_IO_EN = ys.IdString("\\IO.EN")
ID_PORT_XT = ys.IdString("\\XT")
ID_PORT_FB = ys.IdString("\\FB")
ID_PARAM_TABLE = ys.IdString("\\TABLE")
ID_PARAM_DEPTH = ys.IdString("\\DEPTH")
ID_PARAM_WIDTH = ys.IdString("\\WIDTH")
ID_PARAM_ST_INV = ys.IdString("\\ST.INV")
ID_ATTR_INV_OUTPUT = ys.IdString("$inv_output")
ID_ATTR_MC = ys.IdString("$mc")
ID_ATTR_LOGIC_FUNC = ys.IdString("$logic_func")
ID_ATTR_SOP = ys.IdString("$sop")


def get_database():
    for path in sys.path:
        file = os.path.join(path, "database.json")
        if os.path.isfile(file):
            with open(file) as f:
                return json.load(f)
    return None


def get_template_jed(device: str) -> Tuple:
    for path in sys.path:
        file = os.path.join(path, "templates", f"{device}.jed")
        if os.path.isfile(file):
            with open(file, "r") as f:
                return read_jed(f)
    return (None, None)


def sigbit_str(sigbit: ys.SigBit) -> str:
    if sigbit.is_wire():
        return f"{sigbit.wire.name.str()}[{sigbit.offset}]"
    return f"{sigbit.data}"


def sigspec_str(sigspec: ys.SigSpec) -> str:
    return f"{[sigbit_str(b) for b in sigspec.to_sigbit_vector()]}"


def get_cell_param(cell: ys.Cell, param: ys.IdString) -> Optional[ys.Const]:
    return cell.parameters.get(param)


def get_cell_port(cell: ys.Cell, name: ys.IdString) -> Optional[ys.SigSpec]:
    # Remember, name must start with \ or $.
    return cell.connections_.get(name)


def get_cell_port_wire(cell: ys.Cell, name: ys.IdString) -> Optional[ys.Wire]:
    # Remember, name must start with \ or $.
    port = get_cell_port(cell, name)
    return port.as_wire() if port is not None else None


def get_cell_port_wire_name(cell: ys.Cell, name: ys.IdString) -> Optional[str]:
    # Remember, name must start with \ or $.
    wire = get_cell_port_wire(cell, name)
    return wire.name.str() if wire is not None else None


def io_func_is(cell: ys.Cell, value: str) -> bool:
    if cell.type.str() != "$__macrocell":
        return False
    if not cell.has_attribute(ID_ATTR_IO_FUNC):
        return False
    return cell.get_string_attribute(ID_ATTR_IO_FUNC) == value


class ATF15xxDevice:
    def __init__(self, device_name: str, variant: str):
        super().__init__()
        self.toolchain = ""  # don't really need this.
        self.device_name = device_name
        self.variant = variant

        db = get_database()
        if db is None:
            raise SystemExit(
                "Couldn't find database.json file from prjbureau. Is your PYTHONPATH set properly?")

        if device_name not in db:
            raise SystemExit(
                f"Device '{device_name}' not found in database.json file from prjbureau. The known devices are: {db.keys()}")
        self.device = db[device_name]

        if variant not in self.device["pins"]:
            raise SystemExit(
                f"Variant '{variant}' for device '{device_name}' not found in database.json file from prjbureau. The known variants for this device are: {self.device['pins'].keys()}")

        self.orig_fuses, self.jed_comment = get_template_jed(device_name)
        if self.orig_fuses is None:
            raise SystemExit(
                f"Template JED file for device {device_name} not found.")

        self.fuses = bitarray(self.orig_fuses)
        device_fuse_count = list(self.device['ranges'].values())[-1][-1]
        if device_fuse_count != len(self.fuses):
            raise SystemExit(f"Device has {device_fuse_count} fuses, template JED file "
                             f"for device has {len(self.fuses)}")

        self.mc_to_pin = self.device["pins"][self.variant]
        self.pin_to_mc = {v: k[1:]
                          for k, v in self.mc_to_pin.items()
                          if k.startswith("M")}
        self.blocks = self.device["blocks"].keys()
        self.mc_to_block = {k[2:]: v["block"]
                            for k, v in self.device["macrocells"].items()}

        specials = self.device["specials"]

        self.mc_to_jtag = {v[1:]: k
                           for k, v in specials.items()
                           if k in ["TDI", "TDO", "TCK", "TMS"] and v.startswith("M")}
        self.available_mcs = [
            mc for mc in self.pin_to_mc.values() if mc not in self.mc_to_jtag]

        # Maps int gpiobuf num to MC.
        self.gpiobuf_to_mc = {}
        self.input_mcs = {}
        self.input_sigs = {}

        # Map of switch name to {block: str, mux: {fuses:[int], values:{signame: int}}}
        # switch name is UIMn
        # signames are GND0, GND1, MCn_FB, Mn_PAD (among other special ones)
        switches = self.device["switches"]

        # Map signames to UIMs, per block
        # For example, for ATF1502AS, PLCC44, sig_to_uim["A"]["M9_PAD"] = [uims...]
        self.sig_to_uim = {}

        for blk in self.device["blocks"].keys():
            self.sig_to_uim[blk] = {}
        for switch, data in switches.items():
            blk = data["block"]
            switch_sigs = data["mux"]["values"].keys()
            for sig in switch_sigs:
                if sig not in self.sig_to_uim[blk]:
                    self.sig_to_uim[blk][sig] = []
                self.sig_to_uim[blk][sig].append(switch)

        self.fuse_specs = []
        self.fuse_settings = []

    def add_gpiobuf(self, ionum: int, mc):
        self.gpiobuf_to_mc[ionum] = mc

    def commit_fuses(self, output_jed: str):
        tool = FuseTool(self.device, self.fuses)

        history = []
        changed = 0

        for selector, value in zip(self.fuse_specs, self.fuse_settings):
            action_changed = tool.set_device(
                parse_filters((selector,), history), value)
            if action_changed == 0:
                raise SystemExit(
                    f"Filter '{selector}' does not match anything")
            changed += action_changed
            self.jed_comment += f"Edited: set {selector} {value}\n"

        changed_fuses = (self.orig_fuses ^ self.fuses).count(1)
        print(f"Changed {changed} fields, {changed_fuses} fuses.")

        if self.fuses != self.orig_fuses:
            with open(output_jed, "w") as f:
                write_jed(f, self.fuses, comment=self.jed_comment)

    def set_fuse(self, spec: str, setting: str):
        self.fuse_specs.append(spec)
        self.fuse_settings.append(setting)
        print(f"  set {spec} {setting}")

    def arm(self):
        self.set_fuse("CFG.arming_switch", "armed")


class ReplaceSopWithNotPass(ys.Pass):
    def __init__(self):
        super().__init__("replace_sop_with_not",
                         "Replaces $sop cells that implement not with $_NOT_ cells")

    def py_help(self):
        ys.log("Replaces $sop cells that implement not with $_NOT_ cells\n")

    def py_execute(self, args, design):
        ys.log_header(design, "Replacing $sop cells equivalent to $_NOT_\n")
        for module in design.selected_whole_modules_warn():
            cells_to_remove = []
            for cell in [cell for cell in module.selected_cells() if cell.type.str() == "$sop"]:
                sop_depth = cell.parameters.get(
                    ys.IdString("\\DEPTH")).as_int()
                sop_width = cell.parameters.get(
                    ys.IdString("\\WIDTH")).as_int()
                sop_table = cell.parameters.get(
                    ys.IdString("\\TABLE")).as_int()
                sop_input = get_cell_port(cell, ID_PORT_A)
                sop_output = get_cell_port(cell, ID_PORT_Y)

                if sop_depth != 1 or sop_width != 1 or sop_table != 1:
                    continue

                not_cell = module.addCell(
                    module.uniquify(ys.IdString("$notsop")),
                    ys.IdString("$_NOT_"))
                not_cell.setPort(ys.IdString("\\A"), sop_input)
                not_cell.setPort(ID_PORT_Y, sop_output)
                ys.log(
                    f"$sop cell {cell.name.str()} replaced with $_NOT_ cell {not_cell.name.str()}\n")
                cells_to_remove.append(cell)

            for cell in cells_to_remove:
                module.remove(cell)

            ys.log(
                f"Replaced {len(cells_to_remove)} $sop cells with $_NOT_ cells.\n")

    def py_clear_flags(self):
        pass


class CoalesceNotWithSopPass(ys.Pass):
    def __init__(self):
        super().__init__("coalesce_not_with_sop",
                         "Coalesces $_NOT_ gates with $sop outputs")

    def py_help(self):
        ys.log("Coalesces $_NOT_ gates with $sop outputs\n")

    def py_execute(self, args, design):
        ys.log_header(design, "Coalescing $_NOT_ gates with $sop outputs\n")
        for module in design.selected_whole_modules_warn():
            # Find all the $_NOT_ cells that are fed by $sop cells, but where the
            # $sop only feeds that $_NOT_ cell, remove the $_NOT_ cell, and add an
            # inversion attribute to the $sop cell.
            cell_inputs = {}  # input wire name -> Set[Cell]
            not_inputs = {}  # input wire name -> Cell
            sop_outputs = {}  # output wire name -> Cell
            for cell in [cell for cell in module.selected_cells()]:
                inputs = get_cell_port(cell, ID_PORT_A).to_sigbit_vector()
                for s in inputs:
                    if not s.is_wire():
                        continue  # It's probably a const
                    name = f"{s.wire.name.str()}[{s.offset}]"
                    if name not in cell_inputs:
                        cell_inputs[name] = set()
                    cell_inputs[name].update([cell])

                if cell.type.str() == "$_NOT_":
                    name = f"{inputs[0].wire.name.str()}[{s.offset}]"
                    not_inputs[name] = cell

                if cell.type.str() == "$sop":
                    output = get_cell_port(
                        cell, ID_PORT_Y).to_sigbit_vector()[0]
                    name = f"{output.wire.name.str()}[{output.offset}]"
                    sop_outputs[name] = cell

            inversions = []  # List[Tuple[$sop Cell, $_NOT_ Cell]]
            for wire_name, cell in not_inputs.items():
                if len(cell_inputs[wire_name]) == 1:
                    if wire_name in sop_outputs:
                        sop = sop_outputs[wire_name]
                        inversions.append((sop, cell))

            cells_to_remove = []
            for sop, not_cell in inversions:
                sop.set_bool_attribute(ID_ATTR_INV_OUTPUT, True)
                # Replace the output wire in the $sop with the output wire from the $_NOT_.
                sop.setPort(ID_PORT_Y, get_cell_port(not_cell, ID_PORT_Y))
                cells_to_remove.append(not_cell)

            for cell in cells_to_remove:
                module.remove(cell)

            ys.log(
                f"Coalesced {len(cells_to_remove)} $_NOT_ cells with $sop cells.\n")

    def py_clear_flags(self):
        pass


class SplitLargeSopPass(ys.Pass):
    def __init__(self):
        super().__init__("split_large_sop",
                         "Splits $sop cells with more product terms than desired")

    def py_help(self):
        ys.log("Splits $sop cells with more product terms than desired.\n")
        ys.log("  Usage: split_large_sop [threshold]\n")
        ys.log("  The default threshold is 5.\n")

    def py_execute(self, args, design):
        ys.log_header(design, "Splitting overly large $sop cells\n")
        threshold = 5
        if len(args) > 1:
            threshold = int(args[1])
        new_cells = 0
        cells_to_remove = []

        for module in design.selected_whole_modules_warn():
            sops = [cell for cell in module.selected_cells()
                    if cell.type.str() == "$sop"]
            for sop in sops:
                # Depth is the number of product terms
                sop_depth = sop.parameters.get(ID_PARAM_DEPTH).as_int()
                if sop_depth <= threshold:
                    continue
                cells_to_remove.append(sop)

                # Width is the number of inputs
                sop_width = sop.parameters.get(ID_PARAM_WIDTH)
                # for (int i = 0; i < sop_depth; i++) {
                # for (int j = 0; j < sop_width; j++)
                # {
                # 	if (sop_table[2 * (i * sop_width + j) + 0])
                # 	{
                # 		and_in_comp.insert(sop_inputs[j]);
                # 	}
                # 	if (sop_table[2 * (i * sop_width + j) + 1])
                # 	{
                # 		and_in_true.insert(sop_inputs[j]);
                # 	}
                # }
                sop_table = sop.parameters.get(ID_PARAM_TABLE)
                sop_inputs = get_cell_port(sop, ID_PORT_A)
                sop_output = get_cell_port(sop, ID_PORT_Y)
                table = sop_table.as_string()
                product_terms = []
                print(f"Table is {table}")
                for i in range(sop_depth):
                    offset = 2*i*sop_width.as_int()
                    size = 2*sop_width.as_int()
                    product_term = table[offset:offset+size]
                    product_terms.append(product_term)
                    print(f"  Term {i}: {product_term}")

                # Rather than create $sops with 5 inputs each and then ORing
                # them together in another $sop, we ripple $sops together.
                new_output = None
                offset = 0
                while offset < sop_depth:
                    is_first = offset == 0
                    is_last = sop_depth-offset < threshold
                    # We can fit N inputs into the first $sop, but only
                    # N-1 inputs into the subsequent $sops because they
                    # ripple their outputs.
                    if is_first:
                        new_inputs = sop_inputs
                        new_product_terms = product_terms[:threshold]
                        offset += threshold
                    else:
                        new_inputs = sop_inputs
                        new_product_terms = [
                            f"{p}00" for p in product_terms[offset:offset+threshold-1]]
                        additional_product_term = f"{'00'*sop_inputs.size()}01"
                        new_inputs.append(new_output)
                        new_product_terms.append(additional_product_term)
                        offset += threshold-1
                    new_width = new_inputs.size()
                    new_depth = len(new_product_terms)
                    print(f"New width: {new_width}")
                    print(f"New depth: {new_depth}")
                    print(f"New product terms: {''.join(new_product_terms)}")
                    new_table = ys.Const.from_string(
                        "".join(new_product_terms))

                    print(
                        f"new inputs for sop: {sigspec_str(new_inputs)}")
                    if is_last:
                        new_output = sop_output
                        print(f"final output: {sigspec_str(new_output)}")
                    else:
                        new_output = ys.SigSpec(module.addWire(
                            module.uniquify(ys.IdString("$smaller_sop_out"))))
                        print(
                            f"new ripple output: {sigspec_str(new_output)}")

                    table = new_table.as_string()
                    print(f"New table: {table}")
                    for i in range(new_depth):
                        off = 2*i*new_width
                        size = 2*new_width
                        product_term = table[off:off+size]
                        print(f"  Term {i}: {product_term}")

                    new_cell = module.addCell(
                        module.uniquify(ys.IdString("$smaller_sop")),
                        ys.IdString("$sop"))
                    new_cell.setPort(ys.IdString("\\A"), new_inputs)
                    new_cell.setPort(ID_PORT_Y, new_output)
                    new_cell.setParam(ys.IdString("\\TABLE"), new_table)
                    new_cell.setParam(ys.IdString("\\DEPTH"),
                                      ys.Const(new_depth, 32))
                    new_cell.setParam(ys.IdString("\\WIDTH"),
                                      ys.Const(new_width, 32))
                    new_cells += 1

            for cell in cells_to_remove:
                module.remove(cell)

            ys.log(
                f"Removed {len(cells_to_remove)} overly large $sop cells and replaced with {new_cells} cells.\n")

    def py_clear_flags(self):
        pass


class AddIOMacrocellsPass(ys.Pass):
    def __init__(self, device: ATF15xxDevice):
        super().__init__("add_io_macrocells",
                         "Adds $__macrocell cells for inputs and outputs")
        self.device = device

    def py_help(self):
        ys.log("Adds $__macrocell cells for inputs and outputs.\n")

    def is_input_pin(self, wire: ys.Wire) -> bool:
        return wire.name.str().startswith("\\pin_$gpiobuf_") and wire.name.str().endswith("__i")

    def is_output_pin(self, wire: ys.Wire) -> bool:
        return wire.name.str().startswith("\\pin_$gpiobuf_") and wire.name.str().endswith("__o")

    def py_execute(self, args, design):
        ys.log_header(design, "Adding IO macrocells\n")
        for module in design.selected_whole_modules_warn():
            tbufs = [cell for cell in module.selected_cells()
                     if cell.type.str() == "$_TBUF_"]
            for tbuf in tbufs:
                tbuf_output = get_cell_port(tbuf, ID_PORT_Y)
                tbuf_enable = get_cell_port(tbuf, ID_PORT_E)
                print(
                    f"TBUF {sigspec_str(tbuf_output)}, enable = {sigspec_str(tbuf_enable)}")
            print(f" -- Number of TBUFS: {len(tbufs)}")
            for wire in module.wires_.values():
                print(
                    f"Wire {wire.name.str()} offset {wire.start_offset} port_id {wire.port_id} input {wire.port_input} output {wire.port_output}")
            output_wires = [
                wire for wire in module.wires_.values() if wire.port_output]
            print(f" -- Number of output wires (ports): {len(output_wires)}")
            i_wires = [wire for wire in module.wires_.values()
                       if self.is_input_pin(wire)]
            o_wires = [wire for wire in module.wires_.values()
                       if self.is_output_pin(wire)]
            print(f" -- Input wires: {len(i_wires)}")
            print(f" -- Output wires: {len(o_wires)}")
            i_ports = []
            o_ports = []
            for conn_from, conn_to in module.connections_:
                if not conn_from.is_wire() or not conn_to.is_wire():
                    continue
                conn_from_name = conn_from.as_wire().name.str()
                conn_to_name = conn_to.as_wire().name.str()
                if self.is_input_pin(conn_from.as_wire()):
                    i_ports.append(conn_to_name)
                if self.is_output_pin(conn_from.as_wire()):
                    o_ports.append(conn_to_name)
                if self.is_input_pin(conn_to.as_wire()):
                    i_ports.append(conn_from_name)
                if self.is_output_pin(conn_to.as_wire()):
                    o_ports.append(conn_from_name)
            print(f" -- Input ports: {i_ports}")
            print(f" -- Output ports: {o_ports}")
            for wire in output_wires:
                n = wire.name.str().split("_")[1]
                mc = self.device.gpiobuf_to_mc[int(n)]
                new_cell = module.addCell(
                    module.uniquify(ys.IdString(f"$mc{n}")),
                    ys.IdString("$__macrocell"))
                new_cell.set_string_attribute(ys.IdString("$gpiobuf"), n)
                new_cell.set_string_attribute(ID_ATTR_MC, mc)
                if wire.name.str() in i_ports:
                    new_cell.setPort(ID_PORT_PAD, ys.SigSpec(wire))
                    new_cell.setPort(ID_PORT_IO_EN, ys.SigSpec(ys.State.S0))
                    new_cell.set_string_attribute(ID_ATTR_IO_FUNC, "input")
                    self.device.input_mcs[wire.name.str()] = mc
                    self.device.input_sigs[wire.name.str()] = f"M{mc}_PAD"
                else:
                    new_cell.setPort(ID_PORT_IO_A, ys.SigSpec(wire))
                    new_cell.setPort(ID_PORT_IO_EN, ys.SigSpec(ys.State.S1))
                    new_cell.set_string_attribute(ID_ATTR_IO_FUNC, "output")
                    self.device.input_mcs[wire.name.str()] = mc
                    # Remove this MC from the list of available MCs
                    self.device.available_mcs.remove(mc)
            ys.log(
                f"Added {len(output_wires)} macrocells ({len(i_ports)} inputs, {len(o_ports)} outputs)\n")

    def py_clear_flags(self):
        pass


class AllocateSOPMacrocellsPass(ys.Pass):
    def __init__(self, device: ATF15xxDevice):
        super().__init__("allocate_sop_macrocells",
                         "Allocates $__macrocell cells for $sop cells")
        self.device = device

    def py_help(self):
        ys.log("Allocates $__macrocell cells for $sop cells.\n")

    def py_execute(self, args, design):
        ys.log_header(design, "Allocating macrocells for SOPs\n")
        for module in design.selected_whole_modules_warn():
            sops = [cell for cell in module.selected_cells()
                    if cell.type.str() == "$sop"]
            mcs = [cell for cell in module.selected_cells()
                   if cell.type.str() == "$__macrocell"]
            print(mcs)
            mcs_by_output = {
                get_cell_port_wire_name(mc, ID_PORT_IO_A): mc for mc in mcs if io_func_is(mc, "output")
            }
            print(mcs_by_output)
            for sop in sops:
                sop_output = get_cell_port_wire_name(sop, ID_PORT_Y)
                if sop_output in mcs_by_output:
                    new_cell = mcs_by_output[sop_output]
                    print(
                        f"Allocate mc {new_cell.get_string_attribute(ys.IdString('$mc'))} for sop {sop.name.str()} (output wire {sop_output})")
                else:
                    if len(self.device.available_mcs) == 0:
                        raise SystemExit("Ran out of macrocells")
                    mc = self.device.available_mcs[-1]
                    self.device.available_mcs = self.device.available_mcs[:-1]
                    new_cell = module.addCell(
                        module.uniquify(ys.IdString(f"$mc{mc}")),
                        ys.IdString("$__macrocell"))
                    new_cell.set_string_attribute(ID_ATTR_MC, mc)
                    new_cell.set_string_attribute(ID_ATTR_IO_FUNC, "input")

                new_cell.set_string_attribute(ID_ATTR_LOGIC_FUNC, "sop")
                new_cell.set_string_attribute(ID_ATTR_SOP, sop.name.str())
                new_cell.setPort(ID_PORT_XT, get_cell_port(sop, ID_PORT_Y))
                new_cell.setPort(ID_PORT_FB, get_cell_port(sop, ID_PORT_Y))
                new_cell.setPort(ID_PORT_A, get_cell_port(sop, ID_PORT_A))
                new_cell.setParam(
                    ID_PARAM_DEPTH, get_cell_param(sop, ID_PARAM_DEPTH))
                new_cell.setParam(
                    ID_PARAM_WIDTH, get_cell_param(sop, ID_PARAM_WIDTH))
                new_cell.setParam(
                    ID_PARAM_TABLE, get_cell_param(sop, ID_PARAM_TABLE))
                new_cell.setParam(
                    ID_PARAM_ST_INV, ys.Const(ys.State.S1 if sop.has_attribute(
                        ID_ATTR_INV_OUTPUT) else ys.State.S0, 1))
                self.device.input_sigs[get_cell_port_wire_name(
                    sop, ID_PORT_Y)] = f"MC{new_cell.get_string_attribute(ID_ATTR_MC)}_FB"

    def py_clear_flags(self):
        pass


class SetUIMPass(ys.Pass):
    def __init__(self, device: ATF15xxDevice):
        super().__init__("set_uims",
                         "Sets UIM multiplexer and product term fuses")
        self.device = device

    def py_help(self):
        ys.log("Sets UIM multiplexer and product term fuses.\n")

    def py_execute(self, args, design):
        ys.log_header(
            design, "Setting UIM multiplexer and product term fuses\n")
        for module in design.selected_whole_modules_warn():
            mcs = [cell for cell in module.selected_cells()
                   if cell.type.str() == "$__macrocell"]
            mcs = [mc for mc in mcs if mc.has_attribute(ID_ATTR_LOGIC_FUNC)]
            mcs = [mc for mc in mcs if mc.get_string_attribute(
                ID_ATTR_LOGIC_FUNC) == "sop"]
            mc_num_to_cell = {
                mc.get_string_attribute(ID_ATTR_MC): mc for mc in mcs}
            block_to_mcs = {block: [] for block in self.device.blocks}
            for mc in mc_num_to_cell.keys():
                block_to_mcs[self.device.mc_to_block[mc]].append(mc)
            print(block_to_mcs)
            print(self.device.input_sigs)

            for blk, mcs in block_to_mcs.items():
                print(f"Constructing set of signals in block {blk}")
                # Construct the set of needed signals.
                sigs = set()
                for mc in mcs:
                    inputs = get_cell_port(
                        mc_num_to_cell[mc], ID_PORT_A).to_sigbit_vector()
                    sigs.update(set(i.wire.name.str() for i in inputs))

                # Convert to ordered array of signames
                sigs = [self.device.input_sigs[s] for s in sigs]
                if len(sigs) == 0:
                    print(f"No used signals in block {blk}")
                    continue
                print(f"Used signals in block {blk}: {sigs}")

                # Construct the set of candidate switches for those signals.
                candidate_switches = set()
                for sig in sigs:
                    candidate_switches.update(
                        set(s for s in self.device.sig_to_uim[blk][sig]))
                # Convert to ordered array
                candidate_switches = [s for s in candidate_switches]
                print(
                    f"Candidate switches in block {blk}: {candidate_switches}")

                # Construct the cost matrix. We assign an different cost per candidate
                # switch to help the algorithm be stable.
                matrix = [[DISALLOWED for _ in range(
                    len(candidate_switches))] for _ in range(len(sigs))]
                for row, sig in enumerate(sigs):
                    cost = 1
                    for candidate_switch in self.device.sig_to_uim[blk][sig]:
                        col = candidate_switches.index(candidate_switch)
                        matrix[row][col] = cost
                        cost += 1
                cost_matrix = make_cost_matrix(
                    matrix, lambda cost: cost if cost != DISALLOWED else DISALLOWED)

                # Assign signals to switches.
                m = Munkres()
                indexes = m.compute(cost_matrix)
                sig_to_switch = {}
                print("Setting UIM fuses")
                for r, c in indexes:
                    v = matrix[r][c]
                    print(f"Set {candidate_switches[c]} to {sigs[r]}")
                    module.set_string_attribute(ys.IdString(
                        f"$fuse.{candidate_switches[c]}"), sigs[r])
                    sig_to_switch[sigs[r]] = candidate_switches[c]

                print(f"Setting product term fuses:")
                for mc in mcs:
                    cell = mc_num_to_cell[mc]
                    if not cell.hasParam(ID_PARAM_TABLE):
                        continue
                    depth = cell.parameters.get(ID_PARAM_DEPTH).as_int()

                    # Width is the number of inputs
                    width = cell.parameters.get(ID_PARAM_WIDTH).as_int()
                    # for (int i = 0; i < sop_depth; i++) {
                    # for (int j = 0; j < sop_width; j++)
                    # {
                    # 	if (sop_table[2 * (i * sop_width + j) + 0])
                    # 	{
                    # 		and_in_comp.insert(sop_inputs[j]);
                    # 	}
                    # 	if (sop_table[2 * (i * sop_width + j) + 1])
                    # 	{
                    # 		and_in_true.insert(sop_inputs[j]);
                    # 	}
                    # }
                    table = cell.parameters.get(ID_PARAM_TABLE).as_string()
                    inputs = get_cell_port(cell, ID_PORT_A).to_sigbit_vector()
                    product_terms = []
                    print(f"  Table for mc {mc} is {table}")
                    for i in range(depth):
                        offset = 2*i*width
                        size = 2*width
                        product_term = table[offset:offset+size]
                        product_terms.append(product_term)
                    for i, term in enumerate(product_terms):
                        print(f"    Term {i}: {term}")
                        fuses = []
                        for j in range(0, len(term)//2):
                            offset = 2*j
                            pattern = term[offset:offset+2]
                            sig = inputs[j].wire.name.str()
                            signame = self.device.input_sigs[sig]
                            uim = sig_to_switch[signame]
                            print(
                                f"      Input {sig} ({signame}) is {pattern}")
                            if pattern[0] == "1":  # negative
                                fuses.append(f"{uim}_N")
                            if pattern[1] == "1":  # positive
                                fuses.append(f"{uim}_P")
                        cell.set_string_attribute(ys.IdString(
                            f"$fuse.MC{mc}.PT{i+1}"), ",".join(fuses))

    def py_clear_flags(self):
        pass


class WriteJEDPass(ys.Pass):
    def __init__(self, device: ATF15xxDevice):
        super().__init__("write_jed",
                         "Writes a JED file")
        self.device = device

    def py_help(self):
        ys.log("Writes a JED file.\n")

    def py_execute(self, args, design):
        ys.log_header(design, f"Writing JED file {args[1]}\n")
        file = args[1]
        for module in design.selected_whole_modules_warn():
            mcs = [cell for cell in module.selected_cells()
                   if cell.type.str() == "$__macrocell"]
            for mc in mcs:
                self.set_fuses_for_mc(mc)
        fuse_attrs = {k.str()[6:]: v.decode_string() for k,
                      v in module.attributes.items() if k.str().startswith("$fuse.")}
        for k, v in fuse_attrs.items():
            self.device.set_fuse(k, v)
        self.device.commit_fuses(args[1])

    def set_fuses_for_mc(self, mc: ys.Cell):
        io_func = mc.get_string_attribute(ID_ATTR_IO_FUNC)
        logic_func = mc.get_string_attribute(ID_ATTR_LOGIC_FUNC)
        mc_name = f"MC{mc.get_string_attribute(ID_ATTR_MC)}"
        inv = get_cell_param(mc, ID_PARAM_ST_INV)
        if logic_func == "sop":
            self.device.set_fuse(f"{mc_name}.pt_power", "on")
            self.device.set_fuse(f"{mc_name}.fb_mux", "comb")
            self.device.set_fuse(f"{mc_name}.xor_a_mux", "sum")
            self.device.set_fuse(f"{mc_name}.xor_b_mux", "VCC_pt12")
            # It's weird, but because we have to feed a 1 into one input of
            # the macrocell's XOR, it naturally inverts. There's another
            # optional inverter after that, so if we want the non-inverted
            # output of the OR gate, we have to turn that inverter on!
            self.device.set_fuse(f"{mc_name}.xor_invert",
                                 f"{'off' if inv == ys.State.S1 else 'on'}")
        fuse_attrs = {k.str()[6:]: v.decode_string() for k,
                      v in mc.attributes.items() if k.str().startswith("$fuse.")}
        for k, v in fuse_attrs.items():
            self.device.set_fuse(k, v)
        if io_func == "input":
            self.device.set_fuse(f"{mc_name}.oe_mux", "GND")
        elif io_func == "output":
            self.device.set_fuse(f"{mc_name}.o_mux", "comb")
            self.device.set_fuse(f"{mc_name}.oe_mux", "VCC_pt5")
            self.device.set_fuse(f"{mc_name}.pt5_func", "as")

    def py_clear_flags(self):
        pass


class ATF15xxPlatform(Platform):
    resources = []  # Will be filled in based on device and package
    connectors = []
    toolchain = None  # selected when creating platform

    def __init__(self, device_name: str, variant: str):
        super().__init__()
        self.toolchain = ""  # don't really need this.
        self.device = ATF15xxDevice(device_name, variant)

        ionum = 0
        for pin, mc in self.device.pin_to_mc.items():
            if mc in self.device.mc_to_jtag:
                continue
            self.device.add_gpiobuf(ionum, mc)
            self.add_resources([Resource("$gpiobuf", ionum, Pins(str(pin)))])
            ionum += 1
        print(f"Total available pins: {ionum}")

    def toolchain_prepare(self, fragment, name, **kwargs):
        rtlil_text, self._name_map = rtlil.convert_fragment(
            fragment, name=name)
        build_dir = "build"
        os.makedirs(build_dir, exist_ok=True)
        with open(f"{build_dir}/{name}.il", "w") as f:
            f.write(rtlil_text)

        # For some reason running abc (which is run in synth) from
        # Python requires yosys-abc at /usr/bin. Maybe because it
        # just takes the exe dir from the currently running executable
        # (/usr/bin/python3)?

        py_register_pass(ReplaceSopWithNotPass())
        py_register_pass(CoalesceNotWithSopPass())
        py_register_pass(SplitLargeSopPass())
        py_register_pass(AddIOMacrocellsPass(self.device))
        py_register_pass(AllocateSOPMacrocellsPass(self.device))
        py_register_pass(SetUIMPass(self.device))
        py_register_pass(WriteJEDPass(self.device))

        ys.Pass.init_register()

        design = ys.Design()
        ys.run_pass(f"read_ilang {build_dir}/{name}.il", design)
        ys.run_pass("delete w:$verilog_initial_trigger", design)
        ys.run_pass("proc", design)
        ys.run_pass("flatten", design)
        ys.run_pass("stat", design)
        ys.run_pass("synth", design)
        py_run_pass("next_pass", design)
        ys.run_pass("clean", design)
        ys.run_pass("opt -full", design)
        ys.run_pass("stat", design)
        ys.run_pass("abc -sop -I 40 -P 5", design)
        ys.run_pass("clean", design)
        ys.run_pass("stat", design)
        ys.run_pass(f"write_ilang {build_dir}/{name}_pass1.il", design)
        py_run_pass("replace_sop_with_not", design)
        py_run_pass("split_large_sop", design)
        ys.run_pass(f"write_ilang {build_dir}/{name}_pass2.il", design)
        py_run_pass("coalesce_not_with_sop", design)
        ys.run_pass(f"write_ilang {build_dir}/{name}_pass3.il", design)
        py_run_pass("add_io_macrocells", design)
        ys.run_pass(f"write_ilang {build_dir}/{name}_pass4.il", design)
        py_run_pass("allocate_sop_macrocells", design)
        ys.run_pass(f"write_ilang {build_dir}/{name}_pass5.il", design)
        py_run_pass("set_uims", design)
        ys.run_pass(f"write_ilang {build_dir}/{name}_pass6.il", design)
        py_run_pass(f"write_jed {build_dir}/out.jed", design)

        plan = BuildPlan(script=f"build_{name}")
        plan.add_file(f"build_{name}.sh", "")
        return plan

    @ property
    def required_tools(self):
        return ["yosys"]

    @ property
    def file_templates(self):
        return self._file_templates

    @ property
    def command_templates(self):
        return self._command_templates
