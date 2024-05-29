// Generated from c:/Users/natanael.quintino/Documents/pycompiler-1/PythonParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PythonParser}.
 */
public interface PythonParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PythonParser#code}.
	 * @param ctx the parse tree
	 */
	void enterCode(PythonParser.CodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#code}.
	 * @param ctx the parse tree
	 */
	void exitCode(PythonParser.CodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(PythonParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(PythonParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#stat_possibility}.
	 * @param ctx the parse tree
	 */
	void enterStat_possibility(PythonParser.Stat_possibilityContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#stat_possibility}.
	 * @param ctx the parse tree
	 */
	void exitStat_possibility(PythonParser.Stat_possibilityContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(PythonParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(PythonParser.FuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(PythonParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(PythonParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#param_case}.
	 * @param ctx the parse tree
	 */
	void enterParam_case(PythonParser.Param_caseContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#param_case}.
	 * @param ctx the parse tree
	 */
	void exitParam_case(PythonParser.Param_caseContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#param_typed}.
	 * @param ctx the parse tree
	 */
	void enterParam_typed(PythonParser.Param_typedContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#param_typed}.
	 * @param ctx the parse tree
	 */
	void exitParam_typed(PythonParser.Param_typedContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#param_default}.
	 * @param ctx the parse tree
	 */
	void enterParam_default(PythonParser.Param_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#param_default}.
	 * @param ctx the parse tree
	 */
	void exitParam_default(PythonParser.Param_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(PythonParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(PythonParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(PythonParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(PythonParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenQuery}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterParenQuery(PythonParser.ParenQueryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenQuery}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitParenQuery(PythonParser.ParenQueryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code boolean}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterBoolean(PythonParser.BooleanContext ctx);
	/**
	 * Exit a parse tree produced by the {@code boolean}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitBoolean(PythonParser.BooleanContext ctx);
	/**
	 * Enter a parse tree produced by the {@code notQuery}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterNotQuery(PythonParser.NotQueryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code notQuery}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitNotQuery(PythonParser.NotQueryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code spaced_queryR}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterSpaced_queryR(PythonParser.Spaced_queryRContext ctx);
	/**
	 * Exit a parse tree produced by the {@code spaced_queryR}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitSpaced_queryR(PythonParser.Spaced_queryRContext ctx);
	/**
	 * Enter a parse tree produced by the {@code spaced_queryLR}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterSpaced_queryLR(PythonParser.Spaced_queryLRContext ctx);
	/**
	 * Exit a parse tree produced by the {@code spaced_queryLR}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitSpaced_queryLR(PythonParser.Spaced_queryLRContext ctx);
	/**
	 * Enter a parse tree produced by the {@code spaced_queryL}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterSpaced_queryL(PythonParser.Spaced_queryLContext ctx);
	/**
	 * Exit a parse tree produced by the {@code spaced_queryL}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitSpaced_queryL(PythonParser.Spaced_queryLContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalQuery}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterLogicalQuery(PythonParser.LogicalQueryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalQuery}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitLogicalQuery(PythonParser.LogicalQueryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code compareExpr}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void enterCompareExpr(PythonParser.CompareExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code compareExpr}
	 * labeled alternative in {@link PythonParser#query}.
	 * @param ctx the parse tree
	 */
	void exitCompareExpr(PythonParser.CompareExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#funcCall}.
	 * @param ctx the parse tree
	 */
	void enterFuncCall(PythonParser.FuncCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#funcCall}.
	 * @param ctx the parse tree
	 */
	void exitFuncCall(PythonParser.FuncCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(PythonParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(PythonParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code null}
	 * labeled alternative in {@link PythonParser#value}.
	 * @param ctx the parse tree
	 */
	void enterNull(PythonParser.NullContext ctx);
	/**
	 * Exit a parse tree produced by the {@code null}
	 * labeled alternative in {@link PythonParser#value}.
	 * @param ctx the parse tree
	 */
	void exitNull(PythonParser.NullContext ctx);
	/**
	 * Enter a parse tree produced by the {@code string}
	 * labeled alternative in {@link PythonParser#value}.
	 * @param ctx the parse tree
	 */
	void enterString(PythonParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code string}
	 * labeled alternative in {@link PythonParser#value}.
	 * @param ctx the parse tree
	 */
	void exitString(PythonParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code number}
	 * labeled alternative in {@link PythonParser#value}.
	 * @param ctx the parse tree
	 */
	void enterNumber(PythonParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by the {@code number}
	 * labeled alternative in {@link PythonParser#value}.
	 * @param ctx the parse tree
	 */
	void exitNumber(PythonParser.NumberContext ctx);
}