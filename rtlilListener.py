# Generated from rtlil.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .rtlilParser import rtlilParser
else:
    from rtlilParser import rtlilParser

from rtlil import *

curr_module = None


# This class defines a complete listener for a parse tree produced by rtlilParser.
class rtlilListener(ParseTreeListener):

    # Enter a parse tree produced by rtlilParser#file_.
    def enterFile_(self, ctx:rtlilParser.File_Context):
        pass

    # Exit a parse tree produced by rtlilParser#file_.
    def exitFile_(self, ctx:rtlilParser.File_Context):
        pass


    # Enter a parse tree produced by rtlilParser#autoidx_stmt.
    def enterAutoidx_stmt(self, ctx:rtlilParser.Autoidx_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#autoidx_stmt.
    def exitAutoidx_stmt(self, ctx:rtlilParser.Autoidx_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#module.
    def enterModule(self, ctx:rtlilParser.ModuleContext):
        pass

    # Exit a parse tree produced by rtlilParser#module.
    def exitModule(self, ctx:rtlilParser.ModuleContext):
        pass


    # Enter a parse tree produced by rtlilParser#module_body.
    def enterModule_body(self, ctx:rtlilParser.Module_bodyContext):
        pass

    # Exit a parse tree produced by rtlilParser#module_body.
    def exitModule_body(self, ctx:rtlilParser.Module_bodyContext):
        pass


    # Enter a parse tree produced by rtlilParser#param_stmt.
    def enterParam_stmt(self, ctx:rtlilParser.Param_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#param_stmt.
    def exitParam_stmt(self, ctx:rtlilParser.Param_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#wire.
    def enterWire(self, ctx:rtlilParser.WireContext):
        pass

    # Exit a parse tree produced by rtlilParser#wire.
    def exitWire(self, ctx:rtlilParser.WireContext):
        pass


    # Enter a parse tree produced by rtlilParser#wire_option.
    def enterWire_option(self, ctx:rtlilParser.Wire_optionContext):
        pass

    # Exit a parse tree produced by rtlilParser#wire_option.
    def exitWire_option(self, ctx:rtlilParser.Wire_optionContext):
        pass


    # Enter a parse tree produced by rtlilParser#conn_stmt.
    def enterConn_stmt(self, ctx:rtlilParser.Conn_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#conn_stmt.
    def exitConn_stmt(self, ctx:rtlilParser.Conn_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#sig_spec.
    def enterSig_spec(self, ctx:rtlilParser.Sig_specContext):
        pass

    # Exit a parse tree produced by rtlilParser#sig_spec.
    def exitSig_spec(self, ctx:rtlilParser.Sig_specContext):
        pass


    # Enter a parse tree produced by rtlilParser#sig_specs.
    def enterSig_specs(self, ctx:rtlilParser.Sig_specsContext):
        pass

    # Exit a parse tree produced by rtlilParser#sig_specs.
    def exitSig_specs(self, ctx:rtlilParser.Sig_specsContext):
        pass


    # Enter a parse tree produced by rtlilParser#cell.
    def enterCell(self, ctx:rtlilParser.CellContext):
        pass

    # Exit a parse tree produced by rtlilParser#cell.
    def exitCell(self, ctx:rtlilParser.CellContext):
        pass


    # Enter a parse tree produced by rtlilParser#cell_body_stmt.
    def enterCell_body_stmt(self, ctx:rtlilParser.Cell_body_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#cell_body_stmt.
    def exitCell_body_stmt(self, ctx:rtlilParser.Cell_body_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#process.
    def enterProcess(self, ctx:rtlilParser.ProcessContext):
        pass

    # Exit a parse tree produced by rtlilParser#process.
    def exitProcess(self, ctx:rtlilParser.ProcessContext):
        pass


    # Enter a parse tree produced by rtlilParser#switch.
    def enterSwitch(self, ctx:rtlilParser.SwitchContext):
        pass

    # Exit a parse tree produced by rtlilParser#switch.
    def exitSwitch(self, ctx:rtlilParser.SwitchContext):
        pass


    # Enter a parse tree produced by rtlilParser#case.
    def enterCase(self, ctx:rtlilParser.CaseContext):
        pass

    # Exit a parse tree produced by rtlilParser#case.
    def exitCase(self, ctx:rtlilParser.CaseContext):
        pass


    # Enter a parse tree produced by rtlilParser#compare.
    def enterCompare(self, ctx:rtlilParser.CompareContext):
        pass

    # Exit a parse tree produced by rtlilParser#compare.
    def exitCompare(self, ctx:rtlilParser.CompareContext):
        pass


    # Enter a parse tree produced by rtlilParser#sync.
    def enterSync(self, ctx:rtlilParser.SyncContext):
        pass

    # Exit a parse tree produced by rtlilParser#sync.
    def exitSync(self, ctx:rtlilParser.SyncContext):
        pass


    # Enter a parse tree produced by rtlilParser#sync_stmt.
    def enterSync_stmt(self, ctx:rtlilParser.Sync_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#sync_stmt.
    def exitSync_stmt(self, ctx:rtlilParser.Sync_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#sync_type.
    def enterSync_type(self, ctx:rtlilParser.Sync_typeContext):
        pass

    # Exit a parse tree produced by rtlilParser#sync_type.
    def exitSync_type(self, ctx:rtlilParser.Sync_typeContext):
        pass


    # Enter a parse tree produced by rtlilParser#update_stmt.
    def enterUpdate_stmt(self, ctx:rtlilParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#update_stmt.
    def exitUpdate_stmt(self, ctx:rtlilParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#assign_stmt.
    def enterAssign_stmt(self, ctx:rtlilParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#assign_stmt.
    def exitAssign_stmt(self, ctx:rtlilParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#attr_stmts.
    def enterAttr_stmts(self, ctx:rtlilParser.Attr_stmtsContext):
        pass

    # Exit a parse tree produced by rtlilParser#attr_stmts.
    def exitAttr_stmts(self, ctx:rtlilParser.Attr_stmtsContext):
        pass


    # Enter a parse tree produced by rtlilParser#attr_stmt.
    def enterAttr_stmt(self, ctx:rtlilParser.Attr_stmtContext):
        pass

    # Exit a parse tree produced by rtlilParser#attr_stmt.
    def exitAttr_stmt(self, ctx:rtlilParser.Attr_stmtContext):
        pass


    # Enter a parse tree produced by rtlilParser#const.
    def enterConst(self, ctx:rtlilParser.ConstContext):
        pass

    # Exit a parse tree produced by rtlilParser#const.
    def exitConst(self, ctx:rtlilParser.ConstContext):
        pass



del rtlilParser