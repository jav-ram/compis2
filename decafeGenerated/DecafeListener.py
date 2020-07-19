# Generated from .\grammars\Decafe.g4 by ANTLR 4.7.2
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


    # Enter a parse tree produced by DecafeParser#varDeclaration.
    def enterVarDeclaration(self, ctx:DecafeParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by DecafeParser#varDeclaration.
    def exitVarDeclaration(self, ctx:DecafeParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by DecafeParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by DecafeParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
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


    # Enter a parse tree produced by DecafeParser#location.
    def enterLocation(self, ctx:DecafeParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafeParser#location.
    def exitLocation(self, ctx:DecafeParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafeParser#expression.
    def enterExpression(self, ctx:DecafeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DecafeParser#expression.
    def exitExpression(self, ctx:DecafeParser.ExpressionContext):
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


    # Enter a parse tree produced by DecafeParser#arith_op.
    def enterArith_op(self, ctx:DecafeParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DecafeParser#arith_op.
    def exitArith_op(self, ctx:DecafeParser.Arith_opContext):
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


