import sys
from antlr4 import *
from Python3Parser import Python3Parser
from Python3ParserVisitor import Python3ParserVisitor
from pyidebug import debug

class VisitorInterp(Python3ParserVisitor):
    globals = {}

    def visitFile_input(self, ctx):
        # Skipping the odd positions that contains \n or <EOF>
        for i in range(0, ctx.getChildCount()):
            input((ctx.getChildCount(), ctx.getText(), i))
            print(self.visit(ctx.getChild(i)))
        return 0
    
    def visitAnnassign(self, ctx:Python3Parser.AnnassignContext):
        for i in range(0, ctx.getChildCount()):
            input((ctx.getChildCount(), ctx.getText(), i))
            print(self.visit(ctx.getChild(i)))
        return 0
    
    def visitSimple_stmt(self, ctx:Python3Parser.AnnassignContext):
        for i in range(0, ctx.getChildCount()):
            input((ctx.getChildCount(), ctx.getText()))
            print(self.visit(ctx.getChild(i)))
        return 0
    
    def visitSingle_input(self, ctx):
        # Skipping the odd positions that contains \n or <EOF>
        for i in range(0, ctx.getChildCount(), 2):
            input((ctx.getChildCount(), ctx.getChild(i).getText()))
            print(self.visit(ctx.getChild(i)))
        return 0

