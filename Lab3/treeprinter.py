import sys
from scanner import lexer
from custom_parser import parser
from structures import (Instructions,
                        Assignment,
                        BinaryExpression,
                        LogicalExpression,
                        MatrixExpression,
                        Variable,
                        Constant,
                        Matrix,
                        Vector,
                        FunctionCall,
                        PrintCall,
                        IfCondition,
                        ElseIfConditions,
                        ElseIfCondition,
                        ForLoop,
                        ForCondition,
                        WhileLoop,
                        Break,
                        Continue,
                        Return,
                        Node)


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


_print = print


def print(indent, *args, **kwargs):
    _print("|  " * indent + " ".join(str(x) for x in args), **kwargs)


def print_value(value, indent=0):
    if isinstance(value, Node):
        value.print_tree(indent)
    else:
        print(indent, value)


class TreePrinter:

    @addToClass(Instructions)
    def print_tree(self, indent=0):
        for instruction in self.instructions:
            instruction.print_tree(indent)

    @addToClass(Assignment)
    def print_tree(self, indent=0):
        print(indent, self.assignment_type)
        print(indent + 1, self.assignment_id)
        self.expression.print_tree(indent + 1)

    @addToClass(BinaryExpression)
    def print_tree(self, indent=0):
        print(indent, self.operation)
        self.left.print_tree(indent + 1)
        self.right.print_tree(indent + 1)

    @addToClass(LogicalExpression)
    def print_tree(self, indent=0):
        print(indent, self.operation)
        self.left.print_tree(indent + 1)
        self.right.print_tree(indent + 1)

    @addToClass(MatrixExpression)
    def print_tree(self, indent=0):
        print(indent, self.operation)
        self.left.print_tree(indent + 1)
        self.right.print_tree(indent + 1)

    @addToClass(Variable)
    def print_tree(self, indent=0):
        print(indent, self.variable_id)

    @addToClass(Constant)
    def print_tree(self, indent=0):
        print(indent, self.const_value)

    @addToClass(Matrix)
    def print_tree(self, indent=0):
        print(indent, "MATRIX")
        for vector in self.vectors:
            vector.print_tree(indent + 1)

    @addToClass(Vector)
    def print_tree(self, indent=0):
        print(indent, "VECTOR")
        for value in self.values:
            value.print_tree(indent + 1)

    @addToClass(FunctionCall)
    def print_tree(self, indent=0):
        print(indent, self.name)
        self.param.print_tree(indent + 1)

    @addToClass(PrintCall)
    def print_tree(self, indent=0):
        print(indent, "PRINT")
        for value in self.values:
            value.print_tree(indent + 1)

    @addToClass(IfCondition)
    def print_tree(self, indent=0):
        print(indent, "IF")
        self.condition.print_tree(indent + 1)
        print(indent, "THEN")
        for instruction in self.instructions:
            instruction.print_tree(indent + 1)
        for elif_branch in self.elif_branches.conditions:
            elif_branch.print_tree(indent)
        print(indent, "ELSE")
        if self.else_branch:
            self.else_branch.print_tree(indent + 1)

    @addToClass(ElseIfConditions)
    def print_tree(self, indent=0):
        for condition in self.conditions:
            condition.print_tree(indent + 1)

    @addToClass(ElseIfCondition)
    def print_tree(self, indent=0):
        print(indent, "ELSEIF")
        self.condition.print_tree(indent + 1)
        if type(self.instructions) == type('str'):
            print_value(self.instructions, indent + 1)
        else:
            self.instructions.print_tree(indent + 1)

    @addToClass(ForLoop)
    def print_tree(self, indent=0):
        print(indent, "FOR")
        self.for_condition.print_tree(indent + 1)
        self.instructions.print_tree(indent + 1)

    @addToClass(ForCondition)
    def print_tree(self, indent=0):
        self.variable.print_tree(indent)
        print(indent, "RANGE")
        self.variable_range_first.print_tree(indent + 1)
        self.variable_range_last.print_tree(indent + 1)

    @addToClass(WhileLoop)
    def print_tree(self, indent=0):
        print(indent, "WHILE")
        self.condition.print_tree(indent + 1)
        self.instructions.print_tree(indent + 1)

    @addToClass(Break)
    def print_tree(self, indent=0):
        print(indent, "BREAK")

    @addToClass(Continue)
    def print_tree(self, indent=0):
        print(indent, "CONTINUE")

    @addToClass(Return)
    def print_tree(self, indent=0):
        print(indent, "RETURN")
        if (self.instruction is not None):
            self.instruction.print_tree(indent+1)

file = open(sys.argv[1], "r")
text = file.read()
ast = parser.parse(text, lexer=lexer)
ast.print_tree()
