// Generated from .\grammars\Decafe.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DecafeParser}.
 */
public interface DecafeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DecafeParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(DecafeParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(DecafeParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(DecafeParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(DecafeParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclaration(DecafeParser.VarDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclaration(DecafeParser.VarDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#structDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterStructDeclaration(DecafeParser.StructDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#structDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitStructDeclaration(DecafeParser.StructDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#varType}.
	 * @param ctx the parse tree
	 */
	void enterVarType(DecafeParser.VarTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#varType}.
	 * @param ctx the parse tree
	 */
	void exitVarType(DecafeParser.VarTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterMethodDeclaration(DecafeParser.MethodDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitMethodDeclaration(DecafeParser.MethodDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#methodType}.
	 * @param ctx the parse tree
	 */
	void enterMethodType(DecafeParser.MethodTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#methodType}.
	 * @param ctx the parse tree
	 */
	void exitMethodType(DecafeParser.MethodTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(DecafeParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(DecafeParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#parameterType}.
	 * @param ctx the parse tree
	 */
	void enterParameterType(DecafeParser.ParameterTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#parameterType}.
	 * @param ctx the parse tree
	 */
	void exitParameterType(DecafeParser.ParameterTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(DecafeParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(DecafeParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(DecafeParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(DecafeParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#location}.
	 * @param ctx the parse tree
	 */
	void enterLocation(DecafeParser.LocationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#location}.
	 * @param ctx the parse tree
	 */
	void exitLocation(DecafeParser.LocationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(DecafeParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(DecafeParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void enterMethodCall(DecafeParser.MethodCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void exitMethodCall(DecafeParser.MethodCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#arg}.
	 * @param ctx the parse tree
	 */
	void enterArg(DecafeParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#arg}.
	 * @param ctx the parse tree
	 */
	void exitArg(DecafeParser.ArgContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#op}.
	 * @param ctx the parse tree
	 */
	void enterOp(DecafeParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#op}.
	 * @param ctx the parse tree
	 */
	void exitOp(DecafeParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#p_arith_op}.
	 * @param ctx the parse tree
	 */
	void enterP_arith_op(DecafeParser.P_arith_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#p_arith_op}.
	 * @param ctx the parse tree
	 */
	void exitP_arith_op(DecafeParser.P_arith_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#arith_op}.
	 * @param ctx the parse tree
	 */
	void enterArith_op(DecafeParser.Arith_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#arith_op}.
	 * @param ctx the parse tree
	 */
	void exitArith_op(DecafeParser.Arith_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#rel_op}.
	 * @param ctx the parse tree
	 */
	void enterRel_op(DecafeParser.Rel_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#rel_op}.
	 * @param ctx the parse tree
	 */
	void exitRel_op(DecafeParser.Rel_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#eq_op}.
	 * @param ctx the parse tree
	 */
	void enterEq_op(DecafeParser.Eq_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#eq_op}.
	 * @param ctx the parse tree
	 */
	void exitEq_op(DecafeParser.Eq_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#cond_op}.
	 * @param ctx the parse tree
	 */
	void enterCond_op(DecafeParser.Cond_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#cond_op}.
	 * @param ctx the parse tree
	 */
	void exitCond_op(DecafeParser.Cond_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(DecafeParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(DecafeParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#int_literal}.
	 * @param ctx the parse tree
	 */
	void enterInt_literal(DecafeParser.Int_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#int_literal}.
	 * @param ctx the parse tree
	 */
	void exitInt_literal(DecafeParser.Int_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#char_literal}.
	 * @param ctx the parse tree
	 */
	void enterChar_literal(DecafeParser.Char_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#char_literal}.
	 * @param ctx the parse tree
	 */
	void exitChar_literal(DecafeParser.Char_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafeParser#bool_literal}.
	 * @param ctx the parse tree
	 */
	void enterBool_literal(DecafeParser.Bool_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafeParser#bool_literal}.
	 * @param ctx the parse tree
	 */
	void exitBool_literal(DecafeParser.Bool_literalContext ctx);
}