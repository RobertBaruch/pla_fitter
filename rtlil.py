import re
import string
import sys


from typing import List, Optional, Tuple, Any, Union, Dict

# Run antlr4 -Dlanguage=Python3 rtlil.g4


class Const:
    pass


class ConstValue(Const):
    def __init__(self, val: str):
        self.size = 0
        self.val = ""
        pieces = val.split("'")
        self.set_value(int(pieces[0]), pieces[1])

    def set_value(self, size: int, val: str):
        if len(val) != size:
            raise SystemError(
                f"Size of const ({size}) does not match length of value ({len(val)})")
        if not re.fullmatch("[01xzm-]*", val):
            raise SystemError(
                f"Value for const must only contain characters in the set [01xzm-].")
        self.size = size
        self.val = val

    def __str__(self) -> str:
        return f"{self.size}'{self.val}"


class ConstInt(Const):
    def __init__(self, val: str):
        self.i = int(val)

    def __str__(self) -> str:
        return f"{self.i}"


class ConstString(Const):
    def __init__(self, val: str):
        self.val = val

    def __str__(self) -> str:
        return self.val


class AttributeMixin:
    def add_attribute(self, id: str, c: Const):
        if len(id) == 0 or (id[0] != '\\' and id[0] != '$'):
            raise SystemError("Invalid id. Must start with \\ or $")
        self.attrs[id] = c

    def _attrs_str(self, indent: int) -> str:
        indents = "  " * indent
        return "".join([f"{indents}attribute {k} {v}\n" for k, v in self.attrs.items()])


class ParameterMixin:
    def add_param(self, id: str, c: Optional[Const] = None):
        if len(id) == 0 or (id[0] != '\\' and id[0] != '$'):
            raise SystemError("Invalid id. Must start with \\ or $")
        self.params[id] = c

    def set_param_val(self, id: str, c: Optional[Const] = None):
        if id not in self.params:
            raise SystemError("id for set_param_val not in params")
        self.params[id] = c

    def _params_str(self, indent: int) -> str:
        indents = "  " * indent
        return "".join([f"{indents}parameter {k}"
                        f"{'' if v is None else (' ' + str(v))}\n"
                        for k, v in self.params.items()])


class Wire(AttributeMixin):
    def __init__(self, id: str, attrs: Dict[str, Const], options: Dict[str, int]):
        self.id = id
        self.attrs = attrs
        self.options = options

    def __str__(self) -> str:
        attrs = self._attrs_str(1)
        opts = "".join([f"{k} {v} " for k, v in self.options.items()])
        return f"{attrs}  wire {opts}{self.id}\n"


class SigSpec:
    def __init__(self, typ: str, val: Any):
        self.typ = typ
        self.val = val

    def __str__(self) -> str:
        if self.typ == "const" or self.typ == "id":
            return f"{self.val}"
        if self.typ == "slice":
            end = f":{self.val[2]}" if self.val[2] is not None else ""
            return f"{self.val[0]} [{self.val[1]}{end}]"
        if self.typ == "concat":
            ss = " ".join([f"{s}" for s in self.val])
            return "{" + ss + "}"
        raise SystemError(f"Unknown type for sigspec: {self.typ}")


class Assignment:
    def __init__(self, dest: SigSpec, src: SigSpec):
        self.dest = dest
        self.src = src

    def __str__(self) -> str:
        return self._pretty_str(0)

    def _pretty_str(self, indent: int) -> str:
        indents = "  " * indent
        return f"{indents}assign {self.dest} {self.src}\n"


class Connection:
    def __init__(self, sigspec1: SigSpec, sigspec2: SigSpec):
        self.sigspec1 = sigspec1
        self.sigspec2 = sigspec2

    def __str__(self) -> str:
        return f"connect {self.sigspec1} {self.sigspec2}\n"


class Case(AttributeMixin):
    def __init__(self, compares: List[SigSpec], attrs: Dict[str, Const]):
        self.attrs = attrs
        self.compares = compares
        self.switches = []
        self.assignments = []

    def add_switch(self, s: "Switch"):
        self.switches.append(s)

    def add_assignment(self, s: Assignment):
        self.assignments.append(s)

    def __str__(self) -> str:
        return self._pretty_str(2)

    def _pretty_str(self, indent: int) -> str:
        indents = "  " * indent
        attrs = self._attrs_str(indent)
        cmp = ",".join([f" {c}" for c in self.compares])
        begin = f"{indents}case{cmp}\n"
        assigns = "".join(
            [f"{a._pretty_str(indent+1)}" for a in self.assignments])
        switches = "".join(
            [f"{s._pretty_str(indent+1)}" for s in self.switches])
        return f"{attrs}{begin}{assigns}{switches}"


class Switch(AttributeMixin):
    def __init__(self, sig_spec: SigSpec, attrs: Dict[str, Const]):
        self.sig_spec = sig_spec
        self.attrs = attrs
        self.cases = []

    def add_case(self, c: Case):
        self.cases.append(c)

    def __str__(self) -> str:
        return self._pretty_str(2)

    def _pretty_str(self, indent: int) -> str:
        indents = "  " * indent
        attrs = self._attrs_str(indent)
        begin = f"{indents}switch {self.sig_spec}\n"
        cs = "".join(
            [f"{c._pretty_str(indent+1)}" for c in self.cases])
        end = f"{indents}end\n"
        return f"{attrs}{begin}{cs}{end}"


class Cell(AttributeMixin, ParameterMixin):
    def __init__(self, id: str, typ: str, attrs: Dict[str, Const]):
        self.id = id
        self.typ = typ
        self.attrs = attrs
        self.params = {}
        self.ports = {}

    def add_port(self, id: str, sig_spec: SigSpec):
        self.ports[id] = sig_spec

    def __str__(self) -> str:
        attrs = self._attrs_str(1)
        params = self._params_str(2)
        ports = "".join(
            [f"    connect {id} {s}\n" for id, s in self.ports.items()])
        return f"{attrs}  cell {self.id} {self.typ}\n{params}{ports}  end\n"


class Sync:
    def __init__(self, typ: str, sig_spec: Optional[SigSpec] = None):
        self.typ = typ
        self.sig_spec = sig_spec
        self.updates = []

    def add_update(self, s: Assignment):
        self.updates.add(s)

    def __str__(self) -> str:
        updates = "".join(
            [f"  update {u.dest} {u.src}\n" for u in self.updates])
        if self.typ in ["global", "init", "always"]:
            s = f"sync {self.typ}"
        else:
            s = f"sync {self.typ} {self.sig_spec}"
        return f"  {s}\n{updates}"


class Process(AttributeMixin):
    def __init__(self, id: str, attrs: Dict[str, Const]):
        self.id = id
        self.attrs = attrs
        self.assignments = []
        self.syncs = []
        self.switch = None

    def add_assignment(self, s: Assignment):
        self.assignments.append(s)

    def add_sync(self, s: Sync):
        self.syncs.append(s)

    def set_switch(self, s: Switch):
        self.switch = s

    def __str__(self) -> str:
        attrs = self._attrs_str(1)
        assigns = "".join([f"    {a}" for a in self.assignments])
        syncs = "".join([f"  {s}" for s in self.syncs])
        switch = "" if self.switch is None else str(self.switch)
        return f"{attrs}  process {self.id}\n{assigns}{switch}{syncs}  end\n"


class Module(AttributeMixin, ParameterMixin):
    def __init__(self, id: str, attrs: Dict[str, Const]):
        self.id = id
        self.attrs = attrs
        self.params = {}
        self.wires = []
        self.connections = []
        self.cells = []
        self.processes = []

    def add_wire(self, w: Wire):
        self.wires.append(w)

    def add_connection(self, c: Connection):
        self.connections.append(c)

    def add_cell(self, c: Cell):
        self.cells.append(c)

    def add_process(self, p: Process):
        self.processes.append(p)

    def __str__(self) -> str:
        attrs = self._attrs_str(0)
        params = self._params_str(1)
        wires = "".join([f"{w}" for w in self.wires])
        cells = "".join([f"{c}" for c in self.cells])
        procs = "".join([f"{p}" for p in self.processes])
        connects = "".join([f"  {c}" for c in self.connections])
        return f"{attrs}module {self.id}\n{params}{wires}{cells}{procs}{connects}end\n"
