# Generated from grammars\Decafe.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafeParser import DecafeParser
else:
    from DecafeParser import DecafeParser

# This class defines a complete listener for a parse tree produced by DecafeParser.
class DecafeListener(ParseTreeListener):

    # Enter a parse tree produced by DecafeParser#program.
    def enterProgram(self, ctx:DecafeParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafeParser#program.
    def exitProgram(self, ctx:DecafeParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafeParser#declaration.
    def enterDeclaration(self, ctx:DecafeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by DecafeParser#declaration.
    def exitDeclaration(self, ctx:DecafeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by DecafeParser#classDeclaration.
    def enterClassDeclaration(self, ctx:DecafeParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by DecafeParser#classDeclaration.
    def exitClassDeclaration(self, ctx:DecafeParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by DecafeParser#uniqueVar.
    def enterUniqueVar(self, ctx:DecafeParser.UniqueVarContext):
        pass

    # Exit a parse tree produced by DecafeParser#uniqueVar.
    def exitUniqueVar(self, ctx:DecafeParser.UniqueVarContext):
        pass


    # Enter a parse tree produced by DecafeParser#listVar.
    def enterListVar(self, ctx:DecafeParser.ListVarContext):
        pass

    # Exit a parse tree produced by DecafeParser#listVar.
    def exitListVar(self, ctx:DecafeParser.ListVarContext):
        pass


    # Enter a parse tree produced by DecafeParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by DecafeParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by DecafeParser#structInstantiation.
    def enterStructInstantiation(self, ctx:DecafeParser.StructInstantiationContext):
        pass

    # Exit a parse tree produced by DecafeParser#structInstantiation.
    def exitStructInstantiation(self, ctx:DecafeParser.StructInstantiationContext):
        pass


    # Enter a parse tree produced by DecafeParser#varType.
    def enterVarType(self, ctx:DecafeParser.VarTypeContext):
        pass

    # Exit a parse tree produced by DecafeParser#varType.
    def exitVarType(self, ctx:DecafeParser.VarTypeContext):
        pass


    # Enter a parse tree produced by DecafeParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:DecafeParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafeParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:DecafeParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by DecafeParser#methodType.
    def enterMethodType(self, ctx:DecafeParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by DecafeParser#methodType.
    def exitMethodType(self, ctx:DecafeParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by DecafeParser#parameter.
    def enterParameter(self, ctx:DecafeParser.ParameterContext):
        pass

    # Exit a parse tree produced by DecafeParser#parameter.
    def exitParameter(self, ctx:DecafeParser.ParameterContext):
        pass


    # Enter a parse tree produced by DecafeParser#parameterType.
    def enterParameterType(self, ctx:DecafeParser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by DecafeParser#parameterType.
    def exitParameterType(self, ctx:DecafeParser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by DecafeParser#block.
    def enterBlock(self, ctx:DecafeParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafeParser#block.
    def exitBlock(self, ctx:DecafeParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafeParser#statement.
    def enterStatement(self, ctx:DecafeParser.StatementContext):
        pass

    # Exit a parse tree produced by DecafeParser#statement.
    def exitStatement(self, ctx:DecafeParser.StatementContext):
        pass


    # Enter a parse tree produced by DecafeParser#asignStmt.
    def enterAsignStmt(self, ctx:DecafeParser.AsignStmtContext):
        pass

    # Exit a parse tree produced by DecafeParser#asignStmt.
    def exitAsignStmt(self, ctx:DecafeParser.AsignStmtContext):
        pass


    # Enter a parse tree produced by DecafeParser#ifStmt.
    def enterIfStmt(self, ctx:DecafeParser.IfStmtContext):
        pass

    # Exit a parse tree produced by DecafeParser#ifStmt.
    def exitIfStmt(self, ctx:DecafeParser.IfStmtContext):
        pass


    # Enter a parse tree produced by DecafeParser#elseStmt.
    def enterElseStmt(self, ctx:DecafeParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by DecafeParser#elseStmt.
    def exitElseStmt(self, ctx:DecafeParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by DecafeParser#whileStmt.
    def enterWhileStmt(self, ctx:DecafeParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by DecafeParser#whileStmt.
    def exitWhileStmt(self, ctx:DecafeParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by DecafeParser#returnStmt.
    def enterReturnStmt(self, ctx:DecafeParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by DecafeParser#returnStmt.
    def exitReturnStmt(self, ctx:DecafeParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by DecafeParser#location.
    def enterLocation(self, ctx:DecafeParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafeParser#location.
    def exitLocation(self, ctx:DecafeParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafeParser#methodCallExpr.
    def enterMethodCallExpr(self, ctx:DecafeParser.MethodCallExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#methodCallExpr.
    def exitMethodCallExpr(self, ctx:DecafeParser.MethodCallExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#negationExpr.
    def enterNegationExpr(self, ctx:DecafeParser.NegationExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#negationExpr.
    def exitNegationExpr(self, ctx:DecafeParser.NegationExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#opExpr.
    def enterOpExpr(self, ctx:DecafeParser.OpExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#opExpr.
    def exitOpExpr(self, ctx:DecafeParser.OpExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#eqOpExpr.
    def enterEqOpExpr(self, ctx:DecafeParser.EqOpExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#eqOpExpr.
    def exitEqOpExpr(self, ctx:DecafeParser.EqOpExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#derivedOpExpr.
    def enterDerivedOpExpr(self, ctx:DecafeParser.DerivedOpExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#derivedOpExpr.
    def exitDerivedOpExpr(self, ctx:DecafeParser.DerivedOpExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#relOpExpr.
    def enterRelOpExpr(self, ctx:DecafeParser.RelOpExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#relOpExpr.
    def exitRelOpExpr(self, ctx:DecafeParser.RelOpExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#condOpExpr.
    def enterCondOpExpr(self, ctx:DecafeParser.CondOpExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#condOpExpr.
    def exitCondOpExpr(self, ctx:DecafeParser.CondOpExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#literalExpr.
    def enterLiteralExpr(self, ctx:DecafeParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#literalExpr.
    def exitLiteralExpr(self, ctx:DecafeParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#negativeExpr.
    def enterNegativeExpr(self, ctx:DecafeParser.NegativeExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#negativeExpr.
    def exitNegativeExpr(self, ctx:DecafeParser.NegativeExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#locExpr.
    def enterLocExpr(self, ctx:DecafeParser.LocExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#locExpr.
    def exitLocExpr(self, ctx:DecafeParser.LocExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#parentExpr.
    def enterParentExpr(self, ctx:DecafeParser.ParentExprContext):
        pass

    # Exit a parse tree produced by DecafeParser#parentExpr.
    def exitParentExpr(self, ctx:DecafeParser.ParentExprContext):
        pass


    # Enter a parse tree produced by DecafeParser#arith_op.
    def enterArith_op(self, ctx:DecafeParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DecafeParser#arith_op.
    def exitArith_op(self, ctx:DecafeParser.Arith_opContext):
        pass


    # Enter a parse tree produced by DecafeParser#arith_op_derived.
    def enterArith_op_derived(self, ctx:DecafeParser.Arith_op_derivedContext):
        pass

    # Exit a parse tree produced by DecafeParser#arith_op_derived.
    def exitArith_op_derived(self, ctx:DecafeParser.Arith_op_derivedContext):
        pass


    # Enter a parse tree produced by DecafeParser#methodCall.
    def enterMethodCall(self, ctx:DecafeParser.MethodCallContext):
        pass

    # Exit a parse tree produced by DecafeParser#methodCall.
    def exitMethodCall(self, ctx:DecafeParser.MethodCallContext):
        pass


    # Enter a parse tree produced by DecafeParser#arg.
    def enterArg(self, ctx:DecafeParser.ArgContext):
        pass

    # Exit a parse tree produced by DecafeParser#arg.
    def exitArg(self, ctx:DecafeParser.ArgContext):
        pass


    # Enter a parse tree produced by DecafeParser#op.
    def enterOp(self, ctx:DecafeParser.OpContext):
        pass

    # Exit a parse tree produced by DecafeParser#op.
    def exitOp(self, ctx:DecafeParser.OpContext):
        pass


    # Enter a parse tree produced by DecafeParser#rel_op.
    def enterRel_op(self, ctx:DecafeParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafeParser#rel_op.
    def exitRel_op(self, ctx:DecafeParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafeParser#eq_op.
    def enterEq_op(self, ctx:DecafeParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafeParser#eq_op.
    def exitEq_op(self, ctx:DecafeParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafeParser#cond_op.
    def enterCond_op(self, ctx:DecafeParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DecafeParser#cond_op.
    def exitCond_op(self, ctx:DecafeParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DecafeParser#literal.
    def enterLiteral(self, ctx:DecafeParser.LiteralContext):
        pass

    # Exit a parse tree produced by DecafeParser#literal.
    def exitLiteral(self, ctx:DecafeParser.LiteralContext):
        pass


    # Enter a parse tree produced by DecafeParser#int_literal.
    def enterInt_literal(self, ctx:DecafeParser.Int_literalContext):
        pass

    # Exit a parse tree produced by DecafeParser#int_literal.
    def exitInt_literal(self, ctx:DecafeParser.Int_literalContext):
        pass


    # Enter a parse tree produced by DecafeParser#char_literal.
    def enterChar_literal(self, ctx:DecafeParser.Char_literalContext):
        pass

    # Exit a parse tree produced by DecafeParser#char_literal.
    def exitChar_literal(self, ctx:DecafeParser.Char_literalContext):
        pass


    # Enter a parse tree produced by DecafeParser#bool_literal.
    def enterBool_literal(self, ctx:DecafeParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DecafeParser#bool_literal.
    def exitBool_literal(self, ctx:DecafeParser.Bool_literalContext):
        pass


