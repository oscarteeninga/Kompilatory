import sys
from typechecker import *
from interpreter import *
from custom_parser import parser
from scanner import lexer

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "example1.m"
    file = open(filename, "r")

    text = file.read()
    tokens = parser.parse(text, lexer=lexer)
    checker = TypeChecker()
    checker.visit(tokens)
    interpreter = Interpreter()
    interpreter.visit(tokens)
