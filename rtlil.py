import re
import string
import sys

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Any, Union, Dict, TYPE_CHECKING, cast

# Run antlr4 -Dlanguage=Python3 rtlil.g4


class Const(ABC):
    @abstractmethod
    def size(self) -> int:
        pass


class ConstValue(Const):
    def __init__(self, val: str):
        self.width = 0
        self.val = ""
        pieces = val.split("'")
        self.set_value(int(pieces[0]), pieces[1])

    def set_value(self, width: int, val: str):
        if len(val) != width:
            raise SystemError(
                f"Width of const ({width}) does not match length of value ({len(val)})")
        if not re.fullmatch("[01xzm-]*", val):
            raise SystemError(
                f"Value for const must only contain characters in the set [01xzm-].")
        self.width = width
        self.val = val

    def __str__(self) -> str:
        return f"{self.width}'{self.val}"

    def size(self) -> int:
        return self.width


class ConstInt(Const):
    def __init__(self, val: int):
        self.i = val

    def __str__(self) -> str:
        return f"{self.i}"

    def size(self) -> int:
        return 32


class ConstString(Const):
    def __init__(self, val: str):
        self.val = val

    def __str__(self) -> str:
        return self.val

    def size(self) -> int:
        return len(self.val)


if TYPE_CHECKING:
    class Attributes:
        def __init__(self):
            self.attrs: Dict[str, Const] = {}
    attribute_mixin_base = Attributes
else:
    attribute_mixin_base = object


class AttributeMixin(attribute_mixin_base):
    def set_attribute(self, id: str, c: Optional[Const]):
        if len(id) == 0 or (id[0] != '\\' and id[0] != '$'):
            raise SystemError("Invalid id. Must start with \\ or $")
        if c is None:
            del self.attrs[id]
        else:
            self.attrs[id] = c

    def set_bool_attribute(self, id: str, b: Optional[bool]):
        """Sets a bool attribute.

        Setting it to False is the same as setting it to None: it deletes
        the attribute.
        """
        self.set_attribute(id, None if not b else ConstInt(1))

    def _attrs_str(self, indent: int) -> str:
        indents = "  " * indent
        return "".join([f"{indents}attribute {k} {v}\n" for k, v in self.attrs.items()])


if TYPE_CHECKING:
    class Parameters:
        def __init__(self):
            self.params: Dict[str, Optional[Const]] = {}
    parameter_mixin_base = Parameters
else:
    parameter_mixin_base = object


class ParameterMixin(parameter_mixin_base):
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
    def __init__(self, id: str, attrs: Dict[str, Const] = {}, options: Dict[str, int] = {}):
        self.id = id
        self.attrs = attrs
        self.options = options

    def __str__(self) -> str:
        attrs = self._attrs_str(1)
        opts = "".join([f"{k} {v} " for k, v in self.options.items()])
        return f"{attrs}  wire {opts}{self.id}\n"

    def size(self) -> int:
        return self.options.get("width", 1)


class SigSpec(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def bits(self) -> List["SigSpec"]:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_wire(self) -> bool:
        pass


class ConstSigSpec(SigSpec):
    def __init__(self, c: Const):
        self.c = c

    def size(self) -> int:
        return self.c.size()

    def is_wire(self) -> bool:
        return False

    def __str__(self) -> str:
        return str(self.c)

    def bits(self) -> List["SigSpec"]:
        if self.size() == 1:
            return [self]
        return [SliceSigSpec(self, i) for i in range(self.size())]


class WireSigSpec(SigSpec):
    def __init__(self, w: Wire):
        self.w = w

    def size(self) -> int:
        return self.w.size()

    def is_wire(self) -> bool:
        return True

    def __str__(self) -> str:
        return self.w.id

    def bits(self) -> List["SigSpec"]:
        if self.size() == 1:
            return [self]
        return [SliceSigSpec(self, i) for i in range(self.size())]


class ConcatSigSpec(SigSpec):
    def __init__(self, ss: List[SigSpec]):
        self.sigs = ss

    def size(self) -> int:
        s: int = 0
        for v in self.sigs:
            s += v.size()
        return s

    def is_wire(self) -> bool:
        return all([s.is_wire() for s in self.sigs])

    def __str__(self) -> str:
        ss = " ".join([str(s) for s in self.sigs])
        return "{" + ss + "}"

    def bits(self) -> List["SigSpec"]:
        ps = []
        for s in self.sigs:
            ps.extend(s.bits())
        return ps


class SliceSigSpec(SigSpec):
    def __init__(self, s: SigSpec, start: int, end: Optional[int] = None):
        self.s = s
        self.start = start
        self.end = end

    def size(self) -> int:
        if self.end is None:
            return 1
        return self.end - self.start

    def is_wire(self) -> bool:
        if isinstance(self.s, WireSigSpec):
            return True
        if isinstance(self.s, ConstSigSpec):
            return False
        # There really isn't any good way of determining this except
        # by converting the underlying signal to bits, getting the
        # range, and making sure every bit is from a wire.
        end = self.end if self.end is not None else self.start + 1
        bs = self.bits()[:end-self.start]
        return all([s.is_wire() for s in bs])

    def __str__(self) -> str:
        end = f":{self.end}" if self.end is not None else ""
        return f"{self.s} [{self.start}{end}]"

    def bits(self) -> List["SigSpec"]:
        end = self.end if self.end is not None else self.start + 1
        if isinstance(self.s, ConcatSigSpec) or isinstance(self.s, SliceSigSpec):
            return self.s.bits()[self.start:end]
        if self.end is None:
            return [self]
        return [SliceSigSpec(self.s, i) for i in range(self.start, self.end)]


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
    def __init__(self, compares: List[SigSpec], attrs: Dict[str, Const] = {}):
        self.attrs = attrs
        self.compares = compares
        self.switches: List[Switch] = []
        self.assignments: List[Assignment] = []

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
    def __init__(self, sig_spec: SigSpec, attrs: Dict[str, Const] = {}):
        self.sig_spec = sig_spec
        self.attrs = attrs
        self.cases: List[Case] = []

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
    def __init__(self, typ: str, id: str, attrs: Dict[str, Const] = {}):
        self.id = id
        self.typ = typ
        self.attrs = attrs
        self.params = {}
        self.ports: Dict[str, SigSpec] = {}

    def set_port(self, id: str, sig_spec: SigSpec):
        self.ports[id] = sig_spec

    def __str__(self) -> str:
        attrs = self._attrs_str(1)
        params = self._params_str(2)
        ports = "".join(
            [f"    connect {id} {s}\n" for id, s in self.ports.items()])
        return f"{attrs}  cell {self.typ} {self.id}\n{params}{ports}  end\n"


class Sync:
    def __init__(self, typ: str, sig_spec: Optional[SigSpec] = None):
        self.typ = typ
        self.sig_spec = sig_spec
        self.updates: List[Assignment] = []

    def add_update(self, s: Assignment):
        self.updates.append(s)

    def __str__(self) -> str:
        updates = "".join(
            [f"  update {u.dest} {u.src}\n" for u in self.updates])
        if self.typ in ["global", "init", "always"]:
            s = f"sync {self.typ}"
        else:
            s = f"sync {self.typ} {self.sig_spec}"
        return f"  {s}\n{updates}"


class Process(AttributeMixin):
    def __init__(self, id: str, attrs: Dict[str, Const] = {}):
        self.id = id
        self.attrs = attrs
        self.assignments: List[Assignment] = []
        self.syncs: List[Sync] = []
        self.switch: Optional[Switch] = None

    def add_assignment(self, s: Assignment):
        self.assignments.append(s)

    def add_sync(self, s: Sync):
        self.syncs.append(s)

    def set_switch(self, s: Optional[Switch]):
        self.switch = s

    def __str__(self) -> str:
        attrs = self._attrs_str(1)
        assigns = "".join([f"    {a}" for a in self.assignments])
        syncs = "".join([f"  {s}" for s in self.syncs])
        switch = "" if self.switch is None else str(self.switch)
        return f"{attrs}  process {self.id}\n{assigns}{switch}{syncs}  end\n"


class Module(AttributeMixin, ParameterMixin):
    def __init__(self, id: str, attrs: Dict[str, Const] = {}):
        self.id = id
        self.attrs = attrs
        self.params: Dict[str, Optional[Const]] = {}
        self.wires: Dict[str, Wire] = {}
        self.connections: List[Connection] = []
        self.cells: Dict[str, Cell] = {}
        self.processes: Dict[str, Process] = {}

    def add_wire(self, w: Wire):
        self.wires[w.id] = w

    def add_connection(self, c: Connection):
        self.connections.append(c)

    def add_cell(self, c: Cell):
        self.cells[c.id] = c

    def add_process(self, p: Process):
        self.processes[p.id] = p

    def cells_of_type(self, t: str) -> List[Cell]:
        return [c for c in self.cells.values() if c.typ == t]

    def id_exists(self, id: str) -> bool:
        return id in self.wires or id in self.cells or id in self.processes

    def uniquify(self, id: str, index: int = 0) -> str:
        """Returns a module-unique ID for the given ID."""
        if len(id) == 0 or (id[0] != '\\' and id[0] != '$'):
            raise SystemError("Invalid id. Must start with \\ or $")

        if index == 0:
            if not self.id_exists(id):
                return id
            index += 1

        while True:
            new_name = f"{id}_{index}"
            if not self.id_exists(new_name):
                return new_name
            index += 1

    def __str__(self) -> str:
        attrs = self._attrs_str(0)
        params = self._params_str(1)
        wires = "".join([str(w) for w in self.wires.values()])
        cells = "".join([str(c) for c in self.cells.values()])
        procs = "".join([str(p) for p in self.processes.values()])
        connects = "".join(["  " + str(c) for c in self.connections])
        return f"{attrs}module {self.id}\n{params}{wires}{cells}{procs}{connects}end\n"


if __name__ == "__main__":
    m = Module("$1")
    w = Wire("$2", options={"width": 4})
    m.add_wire(w)
    w2 = Wire("$3")
    m.add_wire(w2)
    con = ConstValue("3'101")
    c = ConcatSigSpec([WireSigSpec(w), WireSigSpec(w2), ConstSigSpec(con)])
    c2 = ConcatSigSpec([c, WireSigSpec(w)])
    s = SliceSigSpec(c2, 9)
    print(str(s))
    print(f"Bits: {' '.join([str(a) for a in c2.bits()])}")
    print([str(z) for z in s.bits()])
    print(s.is_wire())
