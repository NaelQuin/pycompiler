# Generated from PythonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#start.
    def visitStart(self, ctx:PythonParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#emptyLine.
    def visitEmptyLine(self, ctx:PythonParser.EmptyLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#comment.
    def visitComment(self, ctx:PythonParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignment.
    def visitAssignment(self, ctx:PythonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#compareExp.
    def visitCompareExp(self, ctx:PythonParser.CompareExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#parenExp.
    def visitParenExp(self, ctx:PythonParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#logicalExp.
    def visitLogicalExp(self, ctx:PythonParser.LogicalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#notExp.
    def visitNotExp(self, ctx:PythonParser.NotExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#boolean.
    def visitBoolean(self, ctx:PythonParser.BooleanContext):
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