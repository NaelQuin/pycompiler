import sys
import json
from antlr4 import FileStream, CommonTokenStream
from PythonLexer import PythonLexer as Lexer
from PythonParser import PythonParser as Parser
from compiler_def import Compiler

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
        compiler = Compiler()
        compiler.visit(tree)
        vars = compiler.vars

    return vars

if __name__ == '__main__':
    vars = main(sys.argv)
    print('vars: ', json.dumps(vars, indent=4, separators=(',', ' = ')))