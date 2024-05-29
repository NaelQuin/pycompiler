# Generated from PythonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stat_possibility.
    def visitStat_possibility(self, ctx:PythonParser.Stat_possibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#func.
    def visitFunc(self, ctx:PythonParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#params.
    def visitParams(self, ctx:PythonParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#param_case.
    def visitParam_case(self, ctx:PythonParser.Param_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#param_typed.
    def visitParam_typed(self, ctx:PythonParser.Param_typedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#param_default.
    def visitParam_default(self, ctx:PythonParser.Param_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#type.
    def visitType(self, ctx:PythonParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignment.
    def visitAssignment(self, ctx:PythonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#parenQuery.
    def visitParenQuery(self, ctx:PythonParser.ParenQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#boolean.
    def visitBoolean(self, ctx:PythonParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#notQuery.
    def visitNotQuery(self, ctx:PythonParser.NotQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#spaced_queryR.
    def visitSpaced_queryR(self, ctx:PythonParser.Spaced_queryRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#spaced_queryLR.
    def visitSpaced_queryLR(self, ctx:PythonParser.Spaced_queryLRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#spaced_queryL.
    def visitSpaced_queryL(self, ctx:PythonParser.Spaced_queryLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#logicalQuery.
    def visitLogicalQuery(self, ctx:PythonParser.LogicalQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#compareExpr.
    def visitCompareExpr(self, ctx:PythonParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#funcCall.
    def visitFuncCall(self, ctx:PythonParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#null.
    def visitNull(self, ctx:PythonParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#string.
    def visitString(self, ctx:PythonParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#number.
    def visitNumber(self, ctx:PythonParser.NumberContext):
        return self.visitChildren(ctx)



del PythonParser