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


    # Visit a parse tree produced by PythonParser#importing.
    def visitImporting(self, ctx:PythonParser.ImportingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#asStat.
    def visitAsStat(self, ctx:PythonParser.AsStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#statIndent.
    def visitStatIndent(self, ctx:PythonParser.StatIndentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#statPossibility.
    def visitStatPossibility(self, ctx:PythonParser.StatPossibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#whileLoop.
    def visitWhileLoop(self, ctx:PythonParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#forLoop.
    def visitForLoop(self, ctx:PythonParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#varLoop.
    def visitVarLoop(self, ctx:PythonParser.VarLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#loopList.
    def visitLoopList(self, ctx:PythonParser.LoopListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#iterable.
    def visitIterable(self, ctx:PythonParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#range.
    def visitRange(self, ctx:PythonParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#enumerate.
    def visitEnumerate(self, ctx:PythonParser.EnumerateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#conditional.
    def visitConditional(self, ctx:PythonParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#condition.
    def visitCondition(self, ctx:PythonParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#func.
    def visitFunc(self, ctx:PythonParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#params.
    def visitParams(self, ctx:PythonParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#paramCase.
    def visitParamCase(self, ctx:PythonParser.ParamCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#paramDefault.
    def visitParamDefault(self, ctx:PythonParser.ParamDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#varType.
    def visitVarType(self, ctx:PythonParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignment.
    def visitAssignment(self, ctx:PythonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#operationQuery.
    def visitOperationQuery(self, ctx:PythonParser.OperationQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#boolean.
    def visitBoolean(self, ctx:PythonParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#groupedQuery.
    def visitGroupedQuery(self, ctx:PythonParser.GroupedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#notQuery.
    def visitNotQuery(self, ctx:PythonParser.NotQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#spacedQueryL.
    def visitSpacedQueryL(self, ctx:PythonParser.SpacedQueryLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#spacedQueryLR.
    def visitSpacedQueryLR(self, ctx:PythonParser.SpacedQueryLRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#spacedQueryR.
    def visitSpacedQueryR(self, ctx:PythonParser.SpacedQueryRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#relationExpr.
    def visitRelationExpr(self, ctx:PythonParser.RelationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#queryId.
    def visitQueryId(self, ctx:PythonParser.QueryIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#funcCall.
    def visitFuncCall(self, ctx:PythonParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#tuple.
    def visitTuple(self, ctx:PythonParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#list.
    def visitList(self, ctx:PythonParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#set.
    def visitSet(self, ctx:PythonParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dict.
    def visitDict(self, ctx:PythonParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dictEntry.
    def visitDictEntry(self, ctx:PythonParser.DictEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#unhashable.
    def visitUnhashable(self, ctx:PythonParser.UnhashableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#exprSeq.
    def visitExprSeq(self, ctx:PythonParser.ExprSeqContext):
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


    # Visit a parse tree produced by PythonParser#valueList.
    def visitValueList(self, ctx:PythonParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#valueTuple.
    def visitValueTuple(self, ctx:PythonParser.ValueTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#valueDict.
    def visitValueDict(self, ctx:PythonParser.ValueDictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#valueSet.
    def visitValueSet(self, ctx:PythonParser.ValueSetContext):
        return self.visitChildren(ctx)



del PythonParser