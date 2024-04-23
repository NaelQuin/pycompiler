import sys
import json
from antlr4 import FileStream, CommonTokenStream
from PythonLexer import PythonLexer as Lexer
from PythonParser import PythonParser as Parser
from VisitorInterpreter import VisitorInterpreter as Visitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.start()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
        vars = {}
    else:
        interpreter = Visitor()
        interpreter.visit(tree)
        vars = interpreter.vars
    return vars

if __name__ == '__main__':
    vars = main(sys.argv)
    print('vars:', json.dumps(vars, indent=4, separators=(',', ' = ')))