"""
https://medium.com/analytics-vidhya/antlr-and-code-generation-a71ead442005
http://lab.antlr.org/
https://www.antlr.org/
"""

if "." in __name__:
    from .PythonParser import PythonParser
    from .PythonParserVisitor import PythonParserVisitor
else:
    from PythonParser import PythonParser
    from PythonParserVisitor import PythonParserVisitor

class Compiler(PythonParserVisitor):

    def __init__(self):
        super(PythonParserVisitor, self).__init__()
        self.vars = {}
        return None
    
    # Visit a parse tree produced by PythonParser#emptyLine.
    def visitEmptyLine(self, ctx:PythonParser.EmptyLineContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#start.
    def visitStart(self, ctx:PythonParser.StartContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#comment.
    def visitComment(self, ctx:PythonParser.CommentContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#assignment.
    def visitAssignment(self, ctx:PythonParser.AssignmentContext):
        print(('Here', ctx.getText(), type(ctx)))
        var = ctx.getChild(0)
        value = ctx.getChild(-1)
        self.vars[var.getText()] = self.visit(value)
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
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#string.
    def visitString(self, ctx:PythonParser.StringContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#number.
    def visitNumber(self, ctx:PythonParser.NumberContext):
        print(('Here', ctx.getText(), type(ctx)))
        text = ctx.getText()
        if '.' in text:
            output = float(text)
        elif 'j' in text:
            output = complex(text)
        elif text.startswith('0x') or text.startswith('0o'):
            output = eval(text)
        else:
            output = int(text)
        return output

del PythonParser

# class VisitorInterp(Python3Visitor):
#     globals = {}

#     def visitStart(self, ctx):
#         # Skipping the odd positions that contains \n or <EOF>
#         for i in range(0, ctx.getChildCount(), 2):
#             print(self.visit(ctx.getChild(i)))
#         return 0

#     def visitExpr(self, ctx):
#         if ctx.getChildCount() == 3:
#             if ctx.getChild(0).getText() == "(":
#                 return self.visit(ctx.getChild(1))
#             op = ctx.getChild(1).getText()
#             v1 = self.visit(ctx.getChild(0))
#             v2 = self.visit(ctx.getChild(2))
#             input(ctx.getText())
#             if op == "+":
#                 return v1 + v2
#             elif op == "-":
#                 return v1 - v2
#             elif op == "*":
#                 return v1 * v2
#             elif op == "/":
#                 return v1 / v2
#             elif op == "**":
#                 return v1 ** v2
#             elif op == "%":
#                 return v1 % v2
#             return 0
#         if ctx.getChildCount() == 2:
#             opc = ctx.getChild(0).getText()
#             if opc == "+":
#                 return self.visit(ctx.getChild(1))
#             if opc == "-":
#                 return - self.visit(ctx.getChild(1))
#             return 0
#         if ctx.getChildCount() == 1:
#             return self.visit(ctx.getChild(0))
#         return 0

#     def visitComment(self, ctx):
#         comment = ""
#         for child in ctx.getChildren():
#             text = child.getText()
#             if text == "#":
#                 continue
#             comment += f"{text} "
#         comment = comment.strip()
#         return f"Comment: {comment}"
    
#     def visitAssignment(self, ctx):
#         var = ctx.getChild(0).getText()
#         value = self.visit(ctx.getChild(2))
#         self.globals[var] = value
#         return f"{var} = {value}"

#     def visitNotExp(self, ctx):
#         input(ctx.getText())
#         value = ctx.getChild(1)
#         if value.getChild(0).getText() == "(":
#             v1 = self.visit(value.getChild(1))
#         else:
#             v1 = self.visit(value)
#         return eval(f"not {v1}")
 
#     # Visit a parse tree produced by ExprParser#compareExp.
#     def visitCompareExp(self, ctx):
#         op = self.visit(ctx.getChild(1))
#         v1 = self.visit(ctx.getChild(0))
#         v2 = self.visit(ctx.getChild(2))
#         input((v1, v2, op))
#         return eval(f"{v1} {op} {v2}")


#     # Visit a parse tree produced by ExprParser#parenExp.
#     def visitParenExp(self, ctx):
#         if ctx.getChild(0).getText() == "(":
#             return self.visit(ctx.getChild(1))
#         return self.visit(ctx.getChild(0))


#     # Visit a parse tree produced by ExprParser#logicalExp.
#     def visitLogicalExp(self, ctx):
#         op = self.visit(ctx.getChild(1))
#         v1 = self.visit(ctx.getChild(0))
#         v2 = self.visit(ctx.getChild(2))
#         input((v1, v2, op))
#         return eval(f"{v1} {op} {v2}")

#     def visitValue(self, ctx):
#         text = ctx.getText()
#         if "j" in text:
#             output = self.visitComplex(text)
#         elif "." in text:
#             output = self.visitDouble(text)
#         elif text in ["True", "False"]:
#             output = self.visitBoolean(text)
#         elif "\"" in text or "'" in text:
#             output = self.visitString(text)
#         else:
#             output = self.visitInt(text)
#         return output
#     def visitString(self, ctx):
#         return str(ctx.getText())
#     def visitDouble(self, ctx):
#         return float(ctx.getText())
#     def visitLong(self, ctx):
#         return int(ctx.getText())
#     def visitInt(self, ctx):
#         return int(ctx.getText())
#     def visitComplex(self, ctx):
#         return complex(ctx.getText())
#     def visitBoolean(self, ctx):
#         return eval(ctx.getText())
#     def visitNull(self, ctx):
#         return None