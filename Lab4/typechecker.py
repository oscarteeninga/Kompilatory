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
        visitor = getattr(self, method, self.generic_visit)
        visitor(node)

    def generic_visit(self, node):
        print()


class TypeChecker(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.symbol_table = ScopedSymbolTable("global", 1)
        self.inLoops = 0

    def visit_Instructions(self, node: Instructions):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_Variable(self, node: Variable):
        pass

    def visit_Constant(self, node: Constant):
        pass

    def visit_Assignment(self, node: Assignment):
        self.visit(node.assignment_id)
        op = node.assignment_type

        if isinstance(node.expression, MatrixExpression):
            matrix = self.visit_MatrixExpression(node.expression)
            self.symbol_table.insert(VariableSymbol(node.assignment_id.variable_id, matrix))
            pass
        else:
            self.visit(node.expression)

        if not isinstance(node.assignment_id, Variable):
            self.errors.append("Error: left hand side not a variable")

        if op == "=":
            if isinstance(node.expression, Variable):
                symbol = self.symbol_table.lookup(node.assignment_id.variable_id)
                if symbol:
                    self.symbol_table.insert(VariableSymbol(node.assignment_id.variable_id, symbol.type))
                else:
                    self.errors.append("Error: right hand side not in scope {}".format(node.expression))
            elif isinstance(node.expression, Matrix) or isinstance(node.expression, Constant):
                self.symbol_table.insert(VariableSymbol(node.assignment_id.variable_id, node.expression))
            elif isinstance(node.expression, FunctionCall):
                shape = int(node.expression.param.const_value)
                if node.expression.name == "zeros":
                    self.symbol_table.insert(VariableSymbol(
                        node.assignment_id.variable_id,
                        Matrix([Vector([Constant("0") for i in range(shape)]) for i in range(shape)])
                    ))
                elif node.expression.name == "ones":
                    self.symbol_table.insert(VariableSymbol(
                        node.assignment_id.variable_id,
                        Matrix([Vector([Constant("1") for i in range(shape)]) for i in range(shape)])
                    ))
                elif node.expression.name == "eye":
                    self.symbol_table.insert(VariableSymbol(
                        node.assignment_id.variable_id,
                        Matrix([Vector([Constant(int(i == j)) for i in range(shape)]) for j in range(shape)])
                    ))
        else:
            pass

    def visit_Matrix(self, node: Matrix):
        vector_len = len(node.vectors[0])
        for vector in node.vectors:
            if len(vector) != vector_len:
                self.errors.append("Error: inconsistent matrix dimensions")
            self.visit(vector)

    def visit_Vector(self, node: Vector):
        for element in node.values:
            if not isinstance(element, Constant):
                self.errors.append("Error: matrix element can only contain constant elements")

    def visit_FunctionCall(self, node: FunctionCall):
        self.visit(node.param)
        if isinstance(node.param, Constant):
            if not isinstance(node.param.const_value, int):
                self.errors.append("Error: argument of reserved function call should be integer")
        else:
            self.errors.append("Error: argument of reserved function call should be contant")

    def visit_BinaryExpression(self, node: BinaryExpression):
        self.visit(node.left)
        self.visit(node.right)

        if isinstance(node.left, Variable):
            symbol = self.symbol_table.lookup(node.left.variable_id)
            if not symbol:
                self.errors.append("Error: undefined symbol")
            elif isinstance(symbol.type, Matrix):
                self.errors.append("Error: binary expression works with non-matrix")
        if isinstance(node.right, Variable):
            symbol = self.symbol_table.lookup(node.right.variable_id)
            if not symbol:
                self.errors.append("Error: undefined symbol")
            elif isinstance(symbol.type, Matrix):
                self.errors.append("Error: binary expression works with non-matrix")

    def visit_LogicalExpression(self, node: LogicalExpression):
        self.visit(node.left)
        self.visit(node.right)
        pass

    def visit_MatrixExpression(self, node: MatrixExpression):
        self.visit(node.left)
        self.visit(node.right)
        matrix_1 = None
        matrix_2 = None
        if isinstance(node.left, Variable):
            symbol = self.symbol_table.lookup(node.left.variable_id)
            if not symbol:
                self.errors.append("Error: undefined symbol")
            elif not isinstance(symbol.type, Matrix):
                self.errors.append("Error: matrix expression doesn't work with non-matrix")
            else:
                matrix_1 = symbol.type
        elif isinstance(node.left, Matrix):
            matrix_1 = node.left
        else:
            self.errors.append("Error: const cannot be add to matrix")

        if isinstance(node.right, Variable):
            symbol = self.symbol_table.lookup(node.right.variable_id)
            if not symbol:
                self.errors.append("Error: undefined symbol")
            elif not isinstance(symbol.type, Matrix):
                self.errors.append("Error: matrix expression doesn't work with non-matrix")
            else:
                matrix_2 = symbol.type
        elif isinstance(node.right, Matrix):
            matrix_2 = node.left
        else:
            self.errors.append("Error: const cannot be add to matrix")

        if isinstance(matrix_1, Matrix) and isinstance(matrix_2, Matrix):
            if matrix_1.shape() != matrix_2.shape():
                self.errors.append("Error: uncompatable matrixes")
            else:
                return matrix_1

    def visit_ForLoop(self, node: ForLoop):
        self.inLoops += 1
        self.visit(node.for_condition)
        self.visit(node.instructions)
        self.inLoops -= 1
        pass

    def visit_ForCondition(self, node: ForCondition):
        self.visit(node.variable)
        self.visit(node.variable_range_first)
        self.visit(node.variable_range_last)

    def visit_WhileLoop(self, node: WhileLoop):
        self.inLoops += 1
        self.visit(node.condition)
        self.visit(node.instructions)
        self.inLoops -= 1
        pass

    def visit_IfCondition(self, node: IfCondition):
        self.visit(node.condition)
        self.visit(node.instructions)
        self.visit(node.elif_branches)
        self.visit(node.else_branch)

    def visit_ElseIfConditions(self, node: ElseIfConditions):
        for elseIfCondition in node.conditions:
            self.visit(elseIfCondition)

    def visit_ElseIfCondition(self, node: ElseIfCondition):
        self.visit(node.condition)
        self.visit(node.instructions)

    def visit_Break(self, node: Break):
        if self.inLoops == 0:
            self.errors.append("Error: break outside a loop")

    def visit_Continue(self, node: Continue):
        if self.inLoops == 0:
            self.errors.append("Error: continue outside a loop")


file = open(sys.argv[1], "r")

text = file.read()
tokens = parser.parse(text, lexer=lexer)
checker = TypeChecker()
checker.visit(tokens)

# print(checker.symbol_table)

if checker.any_errors():
    for error in checker.get_errors():
        print(error)
else:
    print("No errors found!")
