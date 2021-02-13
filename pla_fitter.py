# Minimally fits PLA files into an ATF15xx chip.
import json
import os
import pprint
import sys
import textwrap

from typing import List, Dict, Tuple


from munkres import Munkres, make_cost_matrix, DISALLOWED, print_matrix
import pyeda
from pyeda.inter import *
from bitarray import bitarray

# !!!!!!!!!!!!!!!!!!!!!NOTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# You must have bitarray, munkres, and pyeda installed via pip3, and also you must
# have checked out the prjbureau repo (https://github.com/whitequark/prjbureau)
# and added the repo to your PYTHONPATH.

# prjbureau stuff:
from util.fuseconv import read_jed, write_jed
from util.fusecli import FuseTool, parse_filters

# AND-OR PLA files look like this:
#
# .i 12
# .o 8
# .ilb b[0] b[1] b[2] b[3] s[0] s[1] s[2] s[3] a[0] a[1] a[2] a[3]
# .ob x[0] x[1] x[2] x[3] x[4] x[5] x[6] x[7]
# .p 20
# 1---0---0--- 10000000
# 0----0--0--- 10000000
# ...more lines
# .e
#
# Some format information here:
#   http://www.ecs.umass.edu/ece/labs/vlsicad/ece667/links/espresso.5.html
#
# So the format spec is:
# A '#' in the first character of the line is a comment.
# .i %d:
#     Number of input variables
# .o %d:
#     Number of output functions
# .ilb <space-separated signal name list>:
#     Names of input variables. Must come after .i. There must be the same
#     number of names as there is in .i.
# .ob <space-separated signal name list>:
#     Names of output functions. Must come after .o. There must be the same
#     number of names as there is in .o.
# .p %d:
#     Number of product terms. May be ignored.
# .e or .end:
#     Optionally marks end of description.
# Product term line:
#     .i number of 1/0/- characters, followed by whitespace, followed by
#     .o number of 1/0 characters. These are in the same order as the
#     input and output names.

# Note that this kind of PLA file only represents and-or (aka sum-of-products).
# Because we're also interested in xor layers, and also multiple layers, we
# have to use multiples of these files, and also a custom file for xor layers.

# XOR PLA files look like this:
#
# .xor
# .i 4
# .o 2
# .ilb b[0] b[1] b[2] b[3]
# .ob x[0] x[1] x[2] x[3]
# .p 2
# 11-- 10
# --11 01
# .e
#
# Note that the file must have .xor at the top, and then the product term lines
# consist of:
#    .i number of 1/- characters, where 1 indicates an input to an XOR gate,
#    followed by whitespace, followed by .o number of 1/0 characters, where 1
#    indicates an XOR gate output.
#
#    You can only have two inputs per XOR gate, and only one product term line
#    per XOR gate!

# PIN PLA files look like this:
#
# .device <device-name> <package-variant>
# .pins
# .i 4
# .o 2
# .ilb b[0] b[1] b[2] b[3]
# .ob x[0] x[1] x[2] x[3]
# .p
# .pin b[0] 4
# .pin b[1] 5
# ...
# .e
#
# Note that the file must specify the device at the top, then .pins, then
# input and output signal names, then pin numbers for each signal.
#
# Known devices are:
#  ATF1502AS
#  ATF1504AS
#
# Known package variants for these devices are:
#  ATF1502AS:
#    PLCC44
#    TQFP44
#  ATF1504AS:
#    TQFP100
#    PQFP100
#    PLCC84
#    PLCC68
#    TQFP44
#    PLCC44


class ProductTerm():
    ones: List[str]
    zeros: List[str]

    def __init__(self):
        # List of symbolic inputs
        self.ones = []
        self.zeros = []
        self.expr = expr(1)

    def __repr__(self):
        pp = pprint.PrettyPrinter(indent=4)
        return pp.pformat({'ones': self.ones, 'zeros': self.zeros})


class OrTerm():
    products: List[ProductTerm]

    def __init__(self):
        self.products = []
        self.expr = expr(0)

    def __repr__(self):
        pp = pprint.PrettyPrinter(indent=4)
        return pp.pformat({'or_products': self.products, 'expr': self.expr})


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


class PLAParser():
    inputs: List[str]
    outputs: List[str]
    or_terms: Dict[str, OrTerm]
    # If the file is marked with .xor, it's an XOR layer.
    is_xor: bool

    def __init__(self, file: str):
        self.inputs = []
        self.outputs = []
        # A map of symbolic output to OrTerm (or Xor)
        self.or_terms = {}
        self.is_xor = False
        self.is_pins = False
        self.device = ""
        self.variant = ""
        self.pins = {}
        self.filename = file

        with open(file) as f:
            for line in f.readlines():
                if not self.readline(line):
                    break
        print(f"Inputs  : {self.inputs}")
        print(f"Outputs : {self.outputs}")
        pp = pprint.PrettyPrinter(indent=4, depth=3)
        print(f"OR Terms:")
        pprint.pprint(self.or_terms)

    def readline(self, line: str) -> bool:
        """Returns if there are more lines to parse."""
        if line.startswith(".e") or line.startswith(".end"):
            return False

        if line.startswith(".xor"):
            if self.is_pins:
                raise SystemExit(
                    f"Error in {self.filename}: both .pins and .xor specified.")
            self.is_xor = True

        if line.startswith(".pins"):
            if self.is_xor:
                raise SystemExit(
                    f"Error in {self.filename}: both .pins and .xor specified.")
            if self.device == "":
                raise SystemExit(
                    f"Error in {self.filename}: .device must be specified before .pins.")
            self.is_pins = True

        if line.startswith(".device "):
            if self.is_xor:
                raise SystemExit(
                    f"Error in {self.filename}: .device must not be specified in .xor file.")
            if self.is_pins:
                raise SystemExit(
                    f"Error in {self.filename}: .device must not be specified in .xor file.")
            device_spec = line.split()
            if len(device_spec) != 3:
                raise SystemExit(
                    f"Error in {self.filename}: .device not of the format .device <device> <package-variant>")
            self.device = line.split()[1]
            self.variant = line.split()[2]

        if line.startswith(".ilb "):
            self.inputs = line.split()[1:]

        if line.startswith(".ob "):
            self.outputs = line.split()[1:]
            for output in self.outputs:
                self.or_terms[output] = OrTerm()

        if line.startswith(".pin "):
            if not self.is_pins:
                raise SystemExit(
                    f"Error in {self.filename}: .pins must not specified before .pin.")
            if self.device == "":
                raise SystemExit(
                    f"Error in {self.filename}: .device must be specified before .pin.")
            pin = line.split()
            if len(pin) != 3:
                raise SystemExit(
                    f"Error in {self.filename}: .pin not of the format .pin <name> <pin>: {line}")
            self.pins[pin[1]] = pin[2]

        if line.startswith("1") or line.startswith("0") or line.startswith("-"):
            if self.is_pins:
                raise SystemExit(
                    f"Error in {self.filename}: Cannot specify logic in .pins file.")
            if self.is_xor:
                self.read_xor_term(line)
            else:
                self.read_or_term(line)
            return True

        return True

    def read_or_term(self, line: str):
        parts = line.split()
        if len(parts) != 2:
            raise SystemExit(
                f"Error in {self.filename}: Logic line not of the format <inputs> <outputs>: {line}")
        if len(parts[0]) != len(self.inputs):
            raise SystemExit(
                f"Error in {self.filename}: Logic line inputs does not have same number of signals as inputs: {line}")
        if len(parts[1]) != len(self.outputs):
            raise SystemExit(
                f"Error in {self.filename}: Logic line inputs does not have same number of signals as outputs: {line}")

        inputs = parts[0]
        outputs = parts[1]
        product = ProductTerm()
        terms = []
        for i, bit in enumerate(inputs):
            if bit == '0':
                product.zeros.append(self.inputs[i])
                terms.append(Not(self.inputs[i]))
            elif bit == '1':
                product.ones.append(self.inputs[i])
                terms.append(self.inputs[i])
        product.expr = And(*terms)

        for i, bit in enumerate(outputs):
            if bit == '1':
                self.or_terms[self.outputs[i]].products.append(product)
                self.or_terms[self.outputs[i]].expr = Or(
                    self.or_terms[self.outputs[i]].expr, product.expr)

    def read_xor_term(self, line: str):
        parts = line.split()
        if len(parts) != 2:
            raise SystemExit(
                f"Error in {self.filename}: Logic line not of the format <inputs> <outputs>: {line}")
        if len(parts[0]) != len(self.inputs):
            raise SystemExit(
                f"Error in {self.filename}: Logic line inputs does not have same number of signals as inputs: {line}")
        if len(parts[1]) != len(self.outputs):
            raise SystemExit(
                f"Error in {self.filename}: Logic line inputs does not have same number of signals as outputs: {line}")

        inputs = parts[0]
        outputs = parts[1]
        terms = []
        for i, bit in enumerate(inputs):
            if bit == '1':
                terms.append(self.inputs[i])
        for i, bit in enumerate(outputs):
            if bit == '1':
                self.or_terms[self.outputs[i]].expr = Xor(*terms)


class Fitter():
    inputs: List[str]
    or_terms: Dict[str, OrTerm]
    all_or_terms: Dict[str, Dict[str, OrTerm]]
    input_mcs: Dict[str, int]
    input_sigs: Dict[str, str]

    def __init__(self):
        self.device = None
        self.device_name = ""
        self.variant = ""
        self.next_mc = 1
        self.available_mcs = []

        self.inputs = []
        self.outputs = []
        # A map of pinned outputs to macrocell number
        self.pinned_outputs = {}
        # A map of symbolic output to OrTerm
        self.or_terms = {}
        # A map of block to map of MC to OrTerm
        self.all_or_terms = {}
        self.all_or_exprs = {}

        # A map of symbolic input to macrocell number
        self.input_mcs = {}
        # A map of symbolic input to multiplexer signal name
        self.input_sigs = {}
        self.pins = {}

        self.fuse_specs = []
        self.fuse_settings = []

    def set_fuse(self, spec: str, setting: str):
        self.fuse_specs.append(spec)
        self.fuse_settings.append(setting)
        print(f"  set {spec} {setting}")

    def arm(self):
        self.set_fuse("CFG.arming_switch", "armed")

    def map_pins(self):
        print("Mapping pins")

        specials = self.device["specials"]
        mc_to_jtag = {v[1:]: k
                      for k, v in specials.items()
                      if k in ["TDI", "TDO", "TCK", "TMS"] and v.startswith("M")}

        mc_to_pin = self.device["pins"][self.variant]
        pin_to_mc = {v: k[1:]
                     for k, v in mc_to_pin.items()
                     if k.startswith("M")}
        self.available_mcs = [
            mc for mc in pin_to_mc.values() if mc not in mc_to_jtag]

        for sig_name, pin in self.pins.items():
            if pin not in pin_to_mc:
                raise SystemExit(
                    f"Pin {pin} for signal {sig_name} does not correspond to a macrocell.")

            mc = pin_to_mc[pin]

            if mc in mc_to_jtag:
                raise SystemExit(
                    f"Pin {pin} for signal {sig_name} corresponds to a JTAG macrocell, which is not yet supported.")

            if sig_name not in self.inputs and sig_name not in self.outputs:
                raise SystemExit(
                    f"Signal {sig_name}, specified for pin {pin}, does not correspond to any input or output.")

            mc_name = f"MC{mc}"
            if sig_name in self.inputs:
                self.input_mcs[sig_name] = mc
                self.input_sigs[sig_name] = f"M{mc}_PAD"
                print(f"Input {sig_name} is at MC{mc} (pin {pin})")
                self.set_fuse(f"{mc_name}.pt_power", "off")
                self.set_fuse(f"{mc_name}.oe_mux", "GND")
            else:
                self.input_mcs[sig_name] = mc
                print(f"Output {sig_name} is at MC{mc} (pin {pin})")
                self.set_fuse(f"{mc_name}.pt_power", "on")
                self.set_fuse(f"{mc_name}.o_mux", "comb")
                self.set_fuse(f"{mc_name}.oe_mux", "VCC_pt5")
                self.set_fuse(f"{mc_name}.pt5_func", "as")
                # Remove this MC from the list of available MCs
                self.available_mcs.remove(mc)

        self.pinned_outputs = {s: self.input_mcs[s] for s in self.outputs}

        print(f"Available MCs are: {self.available_mcs}")

        # Initialize blocks in all_or_terms
        for block in self.device["blocks"].keys():
            self.all_or_terms[block] = {}
            self.all_or_exprs[block] = {}

    def get_next_mc(self) -> str:
        if len(self.available_mcs) == 0:
            return None
        next_mc = self.available_mcs[0]
        self.available_mcs.remove(next_mc)
        return next_mc

    def map_and_or_layer(self):
        print("Mapping AND-OR layer")
        device = self.device

        for output in self.outputs:
            or_term = self.or_terms[output]
            or_expr = or_term.expr
            inv = False
            print(f"{output} = {or_term.expr}")
            if isinstance(or_expr, pyeda.boolalg.expr.OrOp) and len(or_expr.xs) > 5:
                # Maybe we can invert, and then use the macrocell's inverter to invert
                # the result?
                nor_expr = espresso_exprs(Not(or_term.expr).to_dnf())
                # espresso_expr returns a tuple
                # to_dnf converts an expression to disjunctive normal form
                # (i.e. sum of products).
                nor_expr = nor_expr[0].to_dnf()
                print(f"Try the inverse of this instead: {nor_expr}")
                if isinstance(nor_expr, pyeda.boolalg.expr.OrOp) and len(or_expr.xs) > 5:
                    raise SystemExit(
                        f"ERROR: or-term for {output} needs more than"
                        " one macrocell (5 products), which is not supported yet.")
                or_expr = nor_expr
                inv = True

            if output in self.pinned_outputs:
                mc = self.pinned_outputs[output]
            else:
                mc = self.get_next_mc()
            if mc is None:
                raise SystemExit("Ran out of macrocells")

            mc_name = f"MC{mc}"
            macrocell = device["macrocells"][mc_name]
            block = macrocell["block"]
            print(f"output {output} mapped to {mc_name}.FB in block {block}")
            self.all_or_terms[block][mc_name] = or_term
            self.all_or_exprs[block][mc_name] = or_expr
            self.input_mcs[output] = mc
            self.input_sigs[output] = f"MC{mc}_FB"

            if or_term.expr.is_one():
                self.set_fuse(f"{mc_name}.pt_power", "on")
                self.set_fuse(f"{mc_name}.pt1_mux", "sum")
                self.set_fuse(f"{mc_name}.pt2_mux", "sum")
                self.set_fuse(f"{mc_name}.pt3_mux", "sum")
                self.set_fuse(f"{mc_name}.pt4_mux", "sum")
                self.set_fuse(f"{mc_name}.pt5_mux", "sum")
                self.set_fuse(f"{mc_name}.fb_mux", "comb")
                self.set_fuse(f"{mc_name}.xor_a_mux", "VCC_pt2")
                self.set_fuse(f"{mc_name}.xor_b_mux", "VCC_pt12")
                self.set_fuse(f"{mc_name}.xor_invert", "on")
            elif or_term.expr.is_zero():
                self.set_fuse(f"{mc_name}.pt_power", "on")
                self.set_fuse(f"{mc_name}.pt1_mux", "sum")
                self.set_fuse(f"{mc_name}.pt2_mux", "sum")
                self.set_fuse(f"{mc_name}.pt3_mux", "sum")
                self.set_fuse(f"{mc_name}.pt4_mux", "sum")
                self.set_fuse(f"{mc_name}.pt5_mux", "sum")
                self.set_fuse(f"{mc_name}.fb_mux", "comb")
                self.set_fuse(f"{mc_name}.xor_a_mux", "VCC_pt2")
                self.set_fuse(f"{mc_name}.xor_b_mux", "VCC_pt12")
                self.set_fuse(f"{mc_name}.xor_invert", "off")
            else:
                self.set_fuse(f"{mc_name}.pt_power", "on")
                self.set_fuse(f"{mc_name}.pt1_mux", "sum")
                self.set_fuse(f"{mc_name}.pt2_mux", "sum")
                self.set_fuse(f"{mc_name}.pt3_mux", "sum")
                self.set_fuse(f"{mc_name}.pt4_mux", "sum")
                self.set_fuse(f"{mc_name}.pt5_mux", "sum")
                self.set_fuse(f"{mc_name}.fb_mux", "comb")
                self.set_fuse(f"{mc_name}.xor_a_mux", "sum")
                self.set_fuse(f"{mc_name}.xor_b_mux", "VCC_pt12")

                # It's weird, but because we have to feed a 1 into one input of
                # the macrocell's XOR, it naturally inverts. There's another
                # optional inverter after that, so if we want the non-inverted
                # output of the OR gate, we have to turn that inverter on!
                self.set_fuse(f"{mc_name}.xor_invert",
                              f"{'off' if inv else 'on'}")

        # Now that we've mapped inputs to outputs,
        # add them to the inputs and clear out the outputs.
        self.inputs += self.outputs
        self.outputs = []

        print("Input mcs:")
        pprint.pprint(self.input_mcs)
        print("Input sigs:")
        pprint.pprint(self.input_sigs)

    def map_and_xor_layer(self):
        print("Mapping XOR layer")
        device = self.device

        # For now, map the outputs directly onto MCs starting with
        # the next MC
        for output in self.outputs:
            expr = self.or_terms[output].expr
            assert isinstance(expr, pyeda.boolalg.expr.XorOp)
            if len(expr.xs) != 2:
                print(
                    f"ERROR: xor-term for {output} does not have 2 products, which is not supported yet.")
                return

            if output in self.pinned_outputs:
                mc = self.pinned_outputs[output]
            else:
                mc = self.get_next_mc()
            if mc is None:
                raise SystemExit("Ran out of macrocells")

            mc_name = f"MC{mc}"
            macrocell = device["macrocells"][mc_name]
            block = macrocell["block"]
            print(f"output {output} mapped to {mc_name}.FB in block {block}")
            self.all_or_exprs[block][mc_name] = expr
            self.input_mcs[output] = mc
            self.input_sigs[output] = f"MC{mc}_FB"

            self.set_fuse(f"{mc_name}.pt_power", "on")
            self.set_fuse(f"{mc_name}.pt1_mux", "sum")
            self.set_fuse(f"{mc_name}.pt2_mux", "xor")
            self.set_fuse(f"{mc_name}.pt3_mux", "sum")
            self.set_fuse(f"{mc_name}.pt4_mux", "sum")
            self.set_fuse(f"{mc_name}.pt5_mux", "sum")
            self.set_fuse(f"{mc_name}.fb_mux", "comb")
            self.set_fuse(f"{mc_name}.xor_a_mux", "sum")
            self.set_fuse(f"{mc_name}.xor_b_mux", "VCC_pt12")
            self.set_fuse(f"{mc_name}.xor_invert", "on")

        # Now that we've mapped inputs to outputs,
        # add them to the inputs and clear out the outputs.
        self.inputs += self.outputs
        self.outputs = []

        print("Input mcs:")
        pprint.pprint(self.input_mcs)
        print("Input sigs:")
        pprint.pprint(self.input_sigs)

    def set_uims(self):
        # Collect all MCn_FB and Mn_PAD before choosing UIMs for each block.
        # This is an instance of the assignment problem, which we solve using the
        # Hungarian algorithm, which is O(n^3). The hope is that because the matrix
        # is extremely sparse, the algorithm runs very quickly.

        dev = self.device
        switches = dev["switches"]

        # Map signals to UIMs, per block
        sig_to_uim = {}
        for blk in dev["blocks"].keys():
            sig_to_uim[blk] = {}
        for switch, data in switches.items():
            blk = data["block"]
            switch_sigs = data["mux"]["values"].keys()
            for sig in switch_sigs:
                if sig not in sig_to_uim[blk]:
                    sig_to_uim[blk][sig] = []
                sig_to_uim[blk][sig].append(switch)

        for blk in self.all_or_exprs:
            print(f"Constructing set of signals in block {blk}")
            # Construct the set of needed signals.
            sigs = set()
            for or_expr in self.all_or_exprs[blk].values():
                sigs.update(set(self.input_sigs[str(term)]
                                for term in or_expr.support))

            # Convert to ordered array
            sigs = [s for s in sigs]
            if len(sigs) == 0:
                print(f"No used signals in block {blk}")
                continue
            print(f"Used signals in block {blk}: {sigs}")

            # Construct the set of candidate switches for those signals.
            candidate_switches = set()
            for sig in sigs:
                candidate_switches.update(set(s for s in sig_to_uim[blk][sig]))
            # Convert to ordered array
            candidate_switches = [s for s in candidate_switches]
            print(f"Candidate switches in block {blk}: {candidate_switches}")

            # Construct the cost matrix. We assign an different cost per candidate
            # switch to help the algorithm be stable.
            matrix = [[DISALLOWED for _ in range(
                len(candidate_switches))] for _ in range(len(sigs))]
            for row, sig in enumerate(sigs):
                cost = 1
                for candidate_switch in sig_to_uim[blk][sig]:
                    col = candidate_switches.index(candidate_switch)
                    matrix[row][col] = cost
                    cost += 1
            cost_matrix = make_cost_matrix(
                matrix, lambda cost: cost if cost != DISALLOWED else DISALLOWED)

            # Assign signals to switches.
            m = Munkres()
            indexes = m.compute(cost_matrix)
            sig_to_switch = {}
            # print_matrix(matrix, 'Based on this matrix:')
            print("Setting UIM fuses:")
            for r, c in indexes:
                v = matrix[r][c]
                self.set_fuse(candidate_switches[c], sigs[r])
                sig_to_switch[sigs[r]] = candidate_switches[c]
            # pprint.pprint(sig_to_switch)

            print("Setting product term fuses:")
            for mc_name, or_expr in self.all_or_exprs[blk].items():
                products = or_expr.xs if isinstance(or_expr, pyeda.boolalg.expr.OrOp) or isinstance(
                    or_expr, pyeda.boolalg.expr.XorOp) else [or_expr]

                for ptn, product in enumerate(products):
                    terms = product.xs if isinstance(
                        product, pyeda.boolalg.expr.AndOp) else [product]
                    first_term = True
                    for sig in terms:
                        inv = isinstance(sig, pyeda.boolalg.expr.Complement)
                        sig = str(Not(sig) if inv else sig)
                        uim = sig_to_switch[self.input_sigs[sig]]
                        switch_polarity = "_N" if inv else "_P"
                        add = "" if first_term else "+"
                        self.set_fuse(f"{mc_name}.PT{ptn+1}",
                                      f"{add}{uim}{switch_polarity}")
                        first_term = False


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise SystemExit(textwrap.dedent("""
    Very simple fitter for the ATF15xx series of CPLDs.

    Usage: python3 pla_fitter.py <output-jed-file> <pla-files>...

    The first PLA file should be a pin file, which specifies
    the names of pins of input and output signals.

    Then the next PLA files should contain logic. An xor file
    consists only of 2-input XOR gates, and any other file
    consists only of AND-OR logic.

    Registers are not supported. In fact, many things are not
    supported. Only combinatorial layers of AND-OR and XOR gates
    are supported.

    See the top of pla_filter.py for information about the PLA
    file formats.
    """))

    if len(sys.argv) < 3:
        raise SystemExit("No files, nothing to do")
    db = get_database()

    p = Fitter()
    output_jed = sys.argv[1]
    arm = False

    if len(sys.argv) < 3:
        raise SystemExit("No files, nothing to do")

    for i, arg in enumerate(sys.argv[2:]):
        if arg == "arm":
            arm = True
            continue
        parse = PLAParser(arg)
        p.outputs = parse.outputs
        p.or_terms = parse.or_terms

        if parse.is_pins:
            db = get_database()
            if parse.device not in db:
                raise SystemExit(
                    f"Device {parse.device} is not in the prjbureau database.")

            p.device_name = parse.device
            p.variant = parse.variant
            p.device = db[parse.device]
            p.pins = parse.pins
            p.inputs = parse.inputs
            p.outputs = parse.outputs
            p.map_pins()

        elif parse.is_xor:
            p.map_and_xor_layer()

        else:
            p.map_and_or_layer()

    p.set_uims()

    if arm:
        p.arm()

    orig_fuses, jed_comment = get_template_jed(p.device_name)
    if orig_fuses is None:
        raise SystemExit(
            f"Template JED file for device {p.device_name} not found.")

    fuses = bitarray(orig_fuses)
    device_fuse_count = list(p.device['ranges'].values())[-1][-1]
    if device_fuse_count != len(fuses):
        raise SystemExit(f"Device has {device_fuse_count} fuses, template JED file "
                         f"for device has {len(fuses)}")

    tool = FuseTool(p.device, fuses)

    history = []
    changed = 0

    for selector, value in zip(p.fuse_specs, p.fuse_settings):
        action_changed = tool.set_device(
            parse_filters((selector,), history), value)
        if action_changed == 0:
            raise SystemExit(f"Filter '{selector}' does not match anything")
        changed += action_changed
        jed_comment += f"Edited: set {selector} {value}\n"

    changed_fuses = (orig_fuses ^ fuses).count(1)
    print(f"Changed {changed} fields, {changed_fuses} fuses.")

    if fuses != orig_fuses:
        with open(output_jed, "w") as f:
            write_jed(f, fuses, comment=jed_comment)
