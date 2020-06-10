from memory import *
from exceptions import *
import operator
from structures import *
from visit import *


class Interpreter(object):
    def __init__(self):
        self.scope_stack = [Memory()]

    def in_scope(self, scope_type):
        return any(isinstance(x, scope_type) for x in self.scope_stack)

    def get_variable_value(self, name):
        return self.scope_stack[-1].get(name)

    def visit_or_return(self, value):
        return self.get_variable_value(value) if isinstance(value, str) else value

    def get_all(self):
        for scope in reversed(self.scope_stack):
            print(scope.values)

    @on('node')
    def visit(self, node):
        pass

    @when(Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    @when(PrintCall)
    def visit(self, node):
        for value in node.values:
            print(self.visit(value))

    @when(Constant)
    def visit(self, node):
        return node.const_value

    @when(Variable)
    def visit(self, node):
        return self.get_variable_value(node)

    @when(Assignment)
    def visit(self, node):
        if isinstance(node.expression, Constant):
            self.scope_stack[-1].put(str(node.assignment_id), node.expression.const_value)
        else:
            self.scope_stack[-1].put(str(node.assignment_id), self.visit(node.expression))

    @when(FunctionCall)
    def visit(self, node):
        size = node.param
        if node.name == 'zeros':
            return Matrix([[0] * size for _ in range(size)])
        elif node.name == 'ones':
            return Matrix([[1] * size for _ in range(size)])
        elif node.name == 'eye':
            return Matrix([[0] * i + [1] + [0] * (size - i - 1) for i in range(size)])

    @when(Matrix)
    def visit(self, node):
        return node

    @when(MatrixExpression)
    def visit(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right_operan)
        return OPERATORS[node.operator](left, right)

    @when(ForLoop)
    def visit(self, node):
        loopScope = LoopScope(self.scope_stack[-1])
        self.scope_stack.append(loopScope)

        start, end = self.visit(node.for_condition)
        for i in range(start, end):
            try:
                self.scope_stack[-1].put(str(node.for_condition.variable), i)
                self.visit(node.instructions)
            except ContinueException:
                continue
            except BreakException:
                break

        self.scope_stack.pop()

    @when(ForCondition)
    def visit(self, node):
        self.scope_stack[-1].put(node.variable, self.visit_or_return(node.variable_range_first))
        return self.visit_or_return(node.variable_range_first).const_value, self.visit_or_return(node.variable_range_last).const_value

    @when(IfCondition)
    def visit(self, node):
        if self.visit(node.condition):
            self.visit(node.instructions)
        else:
            self.visit(node.else_instructions)

    @when(LogicalExpression)
    def visit(self, node):
        if isinstance(node.left, Variable):
            left = self.visit(node.left)
        elif isinstance(node.left, Constant):
            left = node.left.const_value
        else:
            left = node.left
        if isinstance(node.right, Variable):
            right = self.visit(node.right)
        elif isinstance(node.right, Constant):
            right = node.right.const_value
        else:
            right = node.right
        return OPERATORS[node.operation](left, right)

    @when(BinaryExpression)
    def visit(self, node):
        if isinstance(node.left, Variable):
            left = self.visit(node.left)
        elif isinstance(node.left, Constant):
            left = node.left.const_value
        else:
            left = node.left
        if isinstance(node.right, Variable):
            right = self.visit(node.right)
        elif isinstance(node.right, Constant):
            right = node.right.const_value
        else:
            right = node.right
        return OPERATORS[node.operation](left, right)

    @when(WhileLoop)
    def visit(self, node):
        while self.visit(node.condition):
            try:
                self.visit(node.instructions)
            except ContinueException:
                continue
            except BreakException:
                break

    @when(Break)
    def visit(self, _node):
        raise BreakException

    @when(Continue)
    def visit(self, _node):
        raise ContinueException


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '&': operator.and_,
    '|': operator.or_,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    '==': operator.eq,
    '.+': operator.add,
    '.*': operator.mul,
    '.-': operator.sub,
    './': operator.truediv
}
