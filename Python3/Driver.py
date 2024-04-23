import sys
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from VisitorInterpreter import VisitorInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.simple_stmt()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
        vars = {}
    else:
        vinterp = VisitorInterp()
        vinterp.visit(tree)
        vars = vinterp.globals
    return vars

if __name__ == '__main__':
    vars = main(sys.argv)
    print(f"{vars = }")