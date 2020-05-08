class Node:
    pass


class Instructions:
    def __init__(self, instructions):
        self.instructions = instructions

    def __add__(self, other):
        self.instructions += other.instructions
        return self

    def __str__(self):
        return "Instructions=(instructions=" + str([str(instruction) for instruction in self.instructions]) + ")"


class Assignment:
    def __init__(self, assignment_id, assignment_type, expression):
        self.assignment_id = assignment_id
        self.assignment_type = assignment_type
        self.expression = expression

    def __str__(self):
        return "Assignment=(id=" + str(self.assignment_id) + ", type=" + self.assignment_type + ", expression=" + str(
            self.expression) + ")"


class BinaryExpression:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def __str__(self):
        return "BinaryExpression=(left=" + str(self.left) + ", operation=" + self.operation + ", right=" + str(
            self.right) + ")"


class LogicalExpression:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def __str__(self):
        return "LogicalExpression=(left=" + str(self.left) + ", operation=" + self.operation + ", right=" + str(
            self.right) + ")"


class MatrixExpression:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def __str__(self):
        return "MatrixExpression=(left=" + str(self.left) + ", operation=" + self.operation + ", right=" + str(
            self.right) + ")"


class Variable:
    def __init__(self, variable_id):
        self.variable_id = variable_id

    def __str__(self):
        return "Variable=(id=" + self.variable_id + ")"


class Constant:
    def __init__(self, const_value):
        self.const_value = const_value

    def __str__(self):
        return "Constant=(id=" + str(self.const_value) + ")"


class Matrix:
    def __init__(self, vectors):
        self.vectors = vectors

    def __str__(self):
        return "Matrix=(vectors=" + str([str(vector) for vector in self.vectors]) + ")"

    def shape(self):
        return (len(self.vectors), len(self.vectors[0]))

class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        self.values += other
        return self

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return "Vector=(values=" + str([str(value) for value in self.values]) + ")"


class FunctionCall:
    def __init__(self, name, param):
        self.name = name
        self.param = param

    def __str__(self):
        return "FunctionCall=(name=" + self.name + ", param=" + str(self.param) + ")"


class PrintCall:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        self.values += other.values
        return self

    def __str__(self):
        return "PrintCall=(values=" + str([str(value) for value in self.values]) + ")"


class IfCondition:
    def __init__(self, condition, instructions, elif_branches, else_branch):
        self.condition = condition
        self.instructions = instructions
        self.elif_branches = elif_branches
        self.else_branch = else_branch

    def __str__(self):
        return "IfCondition=(condition=" + str(self.condition) + ", instructions=" + str(
            [str(instruction) for instruction in self.instructions]) + ", elif_branches=" + str(
            [str(elif_branch) for elif_branch in self.elif_branches.conditions]) + ", else_branch=" + str(
            self.else_branch) + ")"


class ElseIfConditions:
    def __init__(self, conditions):
        self.conditions = conditions

    def __add__(self, other):
        self.conditions += other.conditions
        return self

    def __str__(self):
        return "ElseIfConditions=(conditions=" + str([str(conditions) for conditions in self.conditions]) + ")"


class ElseIfCondition:
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions

    def __str__(self):
        return "ElseIfCondition=(condition=" + str(self.condition) + ", instructions=" + str(self.instructions) + ")"


class ForLoop:
    def __init__(self, for_condition, instructions):
        self.for_condition = for_condition
        self.instructions = instructions

    def __str__(self):
        return "ForLoop=(for_condition=" + str(self.for_condition) + ", instructions=" + str(self.instructions) + ")"


class ForCondition:
    def __init__(self, variable, variable_range_first, variable_range_last):
        self.variable = variable
        self.variable_range_first = variable_range_first
        self.variable_range_last = variable_range_last

    def __str__(self):
        return "ForCondition=(variable=" + str(self.variable) + ", range=" + str(self.variable_range_first) + ":" + str(
            self.variable_range_last) + ")"


class WhileLoop:
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions

    def __str__(self):
        return "WhileLoop=(condition=" + str(self.condition) + ", instructions=" + str(self.instructions) + ")"

class Break:
    def __str__(self):
        return "Break=()"

class Continue:
    def __str__(self):
        return "Continue=()"


class Return:
    def __init__(self, instruction=None):
        self.instruction = instruction

    def __str__(self):
        return "Return=(term=(" + str(self.instruction) + "))"
