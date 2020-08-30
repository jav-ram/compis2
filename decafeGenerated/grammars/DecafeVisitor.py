# Generated from grammars\Decafe.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafeParser import DecafeParser
else:
    from DecafeParser import DecafeParser

# This class defines a complete generic visitor for a parse tree produced by DecafeParser.

class DecafeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DecafeParser#program.
    def visitProgram(self, ctx:DecafeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#declaration.
    def visitDeclaration(self, ctx:DecafeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#classDeclaration.
    def visitClassDeclaration(self, ctx:DecafeParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#uniqueVar.
    def visitUniqueVar(self, ctx:DecafeParser.UniqueVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#listVar.
    def visitListVar(self, ctx:DecafeParser.ListVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#structDeclaration.
    def visitStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#structInstantiation.
    def visitStructInstantiation(self, ctx:DecafeParser.StructInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#varType.
    def visitVarType(self, ctx:DecafeParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:DecafeParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#methodType.
    def visitMethodType(self, ctx:DecafeParser.MethodTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#parameter.
    def visitParameter(self, ctx:DecafeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#parameterType.
    def visitParameterType(self, ctx:DecafeParser.ParameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#block.
    def visitBlock(self, ctx:DecafeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#statement.
    def visitStatement(self, ctx:DecafeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#asignStmt.
    def visitAsignStmt(self, ctx:DecafeParser.AsignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#ifStmt.
    def visitIfStmt(self, ctx:DecafeParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#whileStmt.
    def visitWhileStmt(self, ctx:DecafeParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#returnStmt.
    def visitReturnStmt(self, ctx:DecafeParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#location.
    def visitLocation(self, ctx:DecafeParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#methodCallExpr.
    def visitMethodCallExpr(self, ctx:DecafeParser.MethodCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#negationExpr.
    def visitNegationExpr(self, ctx:DecafeParser.NegationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#opExpr.
    def visitOpExpr(self, ctx:DecafeParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#derivedOpExpr.
    def visitDerivedOpExpr(self, ctx:DecafeParser.DerivedOpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#literalExpr.
    def visitLiteralExpr(self, ctx:DecafeParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#negativeExpr.
    def visitNegativeExpr(self, ctx:DecafeParser.NegativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#locExpr.
    def visitLocExpr(self, ctx:DecafeParser.LocExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#parentExpr.
    def visitParentExpr(self, ctx:DecafeParser.ParentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#arith_op.
    def visitArith_op(self, ctx:DecafeParser.Arith_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#arith_op_derived.
    def visitArith_op_derived(self, ctx:DecafeParser.Arith_op_derivedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#methodCall.
    def visitMethodCall(self, ctx:DecafeParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#arg.
    def visitArg(self, ctx:DecafeParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#op.
    def visitOp(self, ctx:DecafeParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#rel_op.
    def visitRel_op(self, ctx:DecafeParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#eq_op.
    def visitEq_op(self, ctx:DecafeParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#cond_op.
    def visitCond_op(self, ctx:DecafeParser.Cond_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#literal.
    def visitLiteral(self, ctx:DecafeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#int_literal.
    def visitInt_literal(self, ctx:DecafeParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#char_literal.
    def visitChar_literal(self, ctx:DecafeParser.Char_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafeParser#bool_literal.
    def visitBool_literal(self, ctx:DecafeParser.Bool_literalContext):
        return self.visitChildren(ctx)



del DecafeParser