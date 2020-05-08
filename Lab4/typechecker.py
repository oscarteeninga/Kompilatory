import sys
from custom_parser import parser
from scanner import lexer
from symboltable import ScopedSymbolTable, VariableSymbol
from structures import *


class NodeVisitor(object):
    def __init__(self):
        self.errors = []

    def any_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        print(method)
        visitor = getattr(self, method, self.generic_visit)
        visitor(node)

    def generic_visit(self, node):
        print()


class TypeChecker(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.symbol_table = ScopedSymbolTable("global", 1)

    def visit_Instructions(self, node: Instructions):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_Variable(self, node: Variable):
        pass

    def visit_Constant(self, node: Constant):
        pass

    def visit_Assignment(self, node: Assignment):
        self.visit(node.assignment_id)
        self.visit(node.expression)
        op = node.assignment_type

        if op == "=":
            if isinstance(node.expression, Variable):
                # right hand side should be in scope
                symbol = self.symbol_table.lookup(node.assignment_type.id)
                if symbol:
                    self.symbol_table.insert(VariableSymbol(node.assignment_id, symbol.type))
                else:
                    self.errors.append("Error - right hand side not in scope {}".format(node.expression))
            elif isinstance(node.expression, Matrix):
                symbol = VariableSymbol(node.assignment_id, ("MATRIX", node.expression))
                self.symbol_table.insert(symbol)
            elif isinstance(node.expression, Constant):
                self.symbol_table.insert(VariableSymbol(node.assignment_id, ("CONSTANT",)))
        else:
            # assuming *= works like = _ .* _ and we type check only on surface
            pass


    def visit_Matrix(self, node: Matrix):
        vector_len = len(node.vectors[0])
        for vector in node.vectors:
            if len(vector) != vector_len:
                self.errors.append("Error: inconsistent matrix dimensions - {} and {}".format(len(vector), vector_len))
            self.visit(vector)


    def visit_Vector(self, node: Vector):
        for element in node.values:
            is_number_constant = isinstance(element, Constant)
            is_number_variable = False
            # check if name is in scope and if name type is number e.g. row looks like [1, 2, x];
            if not (is_number_constant or is_number_variable):
                self.errors.append("Error: matrix element can only contain integer/float elements")


    def visit_FunctionCall(self, node: FunctionCall):
        self.visit(node.param)
        if isinstance(node.param, Constant):
            # check of param is integer
            if not isinstance(node.param.const_value, int):
                self.errors.append("Error: argument of reserved function call should be integer")
        else:
            self.errors.append("Error: argument of reserved function call should be integer")


    def visit_BinaryOperation(self, node: BinaryExpression):
        # assuming binary ops can be only performed on non-matrix objects
        # check if types are valid for node.left, node.right
        self.visit(node.left)
        self.visit(node.right)
        if isinstance(node.left, Matrix) or isinstance(node.right, Matrix):
            self.errors.append("Error: binary operation are not able for matrix object")



    def visit_LogicalOperation(self, node: LogicalExpression):
        # check if left/right types are legit (e.g. comparable)
        self.visit(node.left)
        self.visit(node.right)
        pass


    def visit_MatrixOperation(self, node: MatrixExpression):
        self.visit(node.left)
        self.visit(node.right)
        if not isinstance(node.left, Matrix) or not isinstance(node.right, Matrix):
            self.errors.append("Error: matrix operation are only able for matrix object")
        if node.operation == ".+":
            if node.left.shape() != node.right.shape():
                self.errors.append("Error: matrix dotadd requires the same matrix sizes")


    def visit_PrintInstruction(self, node: PrintCall):
        for value in node.values:
            self.visit(value)
        # verify correctness of all node values
        pass


    def visit_ForLoop(self, node: ForLoop):
        self.visit(node.enumeration)
        self.visit(node.instructions)
        # it starts to get tricky here with scopes
        pass


    def visit_WhileLoop(self, node: WhileLoop):
        self.visit(node.condition)
        self.visit(node.instructions)
        # and here too
        pass

    def visit_IfCondition(self, node: IfCondition):
        self.visit(node.condition)
        self.visit(node.instruction)
        self.visit(node.else_branch)
        # verify names in scope

file = open(sys.argv[1], "r")

text = file.read()
tokens = parser.parse(text, lexer=lexer)
checker = TypeChecker()
checker.visit(tokens)

if checker.any_errors():
    for error in checker.get_errors():
        print(error)
else:
    print("No errors found!")