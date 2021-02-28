/*
 * To compile this:
 * 1. Download the "ANTLR tool itself" (https://www.antlr.org/download.html). Also java.
 * 2. pip3 install antlr4-python3-runtime
 * 3. Create an alias in this exact way:
 *    alias antlr4='java -Xmx500M -cp "<absolute path to>/antlr-4.9.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
 * 4. Run antlr4 -Dlanguage=Python3 rtlil.g4
 */

grammar rtlil;

@header {
from rtlil import *

curr_module = None
}

file_ returns [ms]:
    {$ms = []}
    autoidx_stmt? 
    (module {$ms.append($module.m)} )* 
    EOF 
    ;

autoidx_stmt : 'autoidx' INT EOL ;

module returns [m]:
    {global curr_module}
    attr_stmts
    'module' ID EOL {$m = Module($ID.text, $attr_stmts.a)}
    {curr_module = $m}
    module_body[$m]
    'end' EOL
    ;

module_body[m] : (
    param_stmt[$m]
    | wire {$m.add_wire($wire.w)}
    | conn_stmt {$m.add_connection($conn_stmt.c)}
    | cell {$m.add_cell($cell.c)}
    | process {$m.add_process($process.p)}
    )* 
    ;

param_stmt[m]:
    'parameter' ID {$m.add_param($ID.text)}
    (const {$m.set_param_val($ID.text, $const.c)} )? 
    EOL
    ;

wire returns [w] locals [opts]:
    {$opts = {}}
    attr_stmts
    'wire' 
    (wire_option {$opts = {**$opts, **$wire_option.o}} )*
    ID EOL
    {$w = Wire($ID.text, $attr_stmts.a, $opts)}
    ;

wire_option returns [o]:
    'width' INT {$o = {"width": int($INT.text)}}
    | 'offset' INT {$o = {"offset": int($INT.text)}}
    | 'input' INT {$o = {"input": int($INT.text)}}
    | 'output' INT {$o = {"output": int($INT.text)}}
    | 'inout' INT {$o = {"inout": int($INT.text)}}
    | 'upto' {$o = {"upto": 1}}
    | 'signed' {$o = {"signed": 1}}
    ;

conn_stmt returns [c]:
    'connect' p=sig_spec w=sig_spec EOL {$c = Connection($p.s, $w.s) }
    ;

sig_spec returns [s]:
    const {$s = ConstSigSpec($const.c) }
    | ID 
    {assert curr_module is not None}
    {if $ID.text not in curr_module.wires:}
    {  raise SystemError(f"Sigspec refers to wire '{$ID.text}' that is not present in its module") }
    {$s = WireSigSpec(curr_module.wires[$ID.text]) }
    | <assoc=right> sig=sig_spec '[' st=INT (':' end=INT)? ']'
      {$s = SliceSigSpec($sig.s, $st.text, $end.text) }
    | '{' sig_specs '}' {$s = ConcatSigSpec($sig_specs.ss) }
    ;

sig_specs returns [ss]:
    {$ss = []}
    (sig_spec {$ss.append($sig_spec.s)} )*
    ;

cell returns [c]:
    attr_stmts
    'cell' typ=ID name=ID EOL {$c = Cell($typ.text, $name.text, $attr_stmts.a)}
    cell_body_stmt[$c]*
    'end' EOL
    ;

cell_body_stmt[c]:
    'parameter' ('signed' | 'real')? ID const EOL {$c.add_param($ID.text, $const.c)}
    | 'connect' ID sig_spec EOL {$c.set_port($ID.text, $sig_spec.s)}
    ;

process returns [p]:
    attr_stmts
    'process' ID EOL {$p = Process($ID.text, $attr_stmts.a)}
    (a1=assign_stmt {$p.add_assignment($a1.s)} )*
    (switch {$p.set_switch($switch.s)} )?
    (a2=assign_stmt {$p.add_assignment($a2.s)} )*
    (sync {$p.add_sync($sync.s)} )*
    'end' EOL
    ;

switch returns [s]:
    attr_stmts
    'switch' sig_spec EOL {$s = Switch($sig_spec.s, $attr_stmts.a)}
    (case {$s.add_case($case.c)} )*
    'end' EOL
    ;

case returns [c]:
    attr_stmts
    'case' compare EOL {$c = Case($compare.ss, $attr_stmts.a)}
    (switch {$c.add_switch($switch.s)}
     | assign_stmt {$c.add_assignment($assign_stmt.s)} 
     )*
    ;

compare returns [ss]:
    {$ss = []}
    ( s1=sig_spec {$ss.append($s1.s)}
      (',' s2=sig_spec {$ss.append($s2.s)} )* 
    )?
    ;

sync returns [s]:
    sync_stmt {$s = $sync_stmt.s}
    (update_stmt {$s.add_update($update_stmt.s)} )*
    ;

sync_stmt returns [s]:
    'sync' sync_type sig_spec EOL {$s = Sync($sync_type.text, $sig_spec.s)}
    | 'sync' 'global' EOL {$s = Sync("global")}
    | 'sync' 'init' EOL {$s = Sync("init")}
    | 'sync' 'always' EOL {$s = Sync("always")}
    ;

sync_type:
    'low' | 'high' | 'posedge' | 'negedge' | 'edge' ;

update_stmt returns [s]:
    'update' dest=sig_spec src=sig_spec EOL
    {$s = Assignment($dest.s, $src.s)}
    ;

assign_stmt returns [s]:
    'assign' dest=sig_spec src=sig_spec EOL
    {$s = Assignment($dest.s, $src.s)}
    ;

attr_stmts returns [a]:
    {$a = {}}
    (attr_stmt {$a[$attr_stmt.i] = $attr_stmt.c} )*
    ;

attr_stmt returns [i, c]:
    'attribute'
    ID {$i = $ID.text}
    const {$c = $const.c}
    EOL
    ;

const returns [c]: 
    VALUE {$c = ConstValue($VALUE.text)} 
    | INT {$c = ConstInt(int($INT.text))} 
    | STRING {$c = ConstString($STRING.text)}
    ;

STRING: '"' .*? '"' ;
ID: ('\\'|'$') [\u0021-\u00FF]+ ;
VALUE: DECIMAL_DIGIT+ '\'' BINARY_DIGIT* ;
INT: '-'? DECIMAL_DIGIT+ ;
EOL: [\r\n]+ ;

SKIP_: ( WS | COMMENT ) -> skip ;
fragment COMMENT: '#' ~[\r\n]* [\r\n] ;
fragment WS: [ \t]+ ;
fragment DECIMAL_DIGIT: [0123456789] ;
fragment BINARY_DIGIT: [01xzm-] ;