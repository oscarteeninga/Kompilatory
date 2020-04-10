import scanner
import ply.yacc as yacc
import sys
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
                        Node
                        )

names = {}

tokens = scanner.tokens

precedence = ()

def p_error(p):
    if p:
        print("Syntax error at line {0}, LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_code(p):
    """
    CODE : INSTRUCTIONS
    """
    p[0] = p[1]


def p_instructions(p):
    """
    INSTRUCTIONS : '{' INSTRUCTIONS '}'
                | INSTRUCTION INSTRUCTIONS
                | INSTRUCTION
    """
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = Instructions(instructions=[p[1]]) + p[2]
    else:
        p[0] = Instructions(instructions=[p[1]])


def p_instruction(p):
    """
    INSTRUCTION : ASSIGN ';'
                | IF_CONDITION
                | FOR_LOOP
                | WHILE_LOOP
                | CONTROL_INSTRUCTION ';'
                | PRINT_CALL ';'
    """
    p[0] = p[1]


def p_assign(p):
    """
    ASSIGN : ID ASSIGN_TYPE EXPRESSION
           | ID '[' INTNUM ']' ASSIGN_TYPE EXPRESSION
           | ID '[' INTNUM ',' INTNUM ']' ASSIGN_TYPE EXPRESSION
    """
    if len(p) == 4:
        p[0] = Assignment(assignment_id=p[1], assignment_type=p[2], expression=p[3])
    elif len(p) == 7:
        p[0] = Assignment(assignment_id=p[1] + '[' + str(p[3]) + ']', assignment_type=p[5], expression=p[6])
    else:
        p[0] = Assignment(assignment_id=p[1] + '[' + str(p[3]) + ',' + str(p[5]) + ']', assignment_type=p[7], expression=p[8])


def p_assign_type(p):
    """
    ASSIGN_TYPE : '='
                | ADDASSIGN
                | SUBASSIGN
                | DIVASSIGN
                | MULASSIGN
    """
    p[0] = p[1]


def p_expression(p):
    """
    EXPRESSION : BINARY_EXPRESSION
               | LOGICAL_EXPRESSION
               | MATRIX_EXPRESSION
               | '(' EXPRESSION ')'
               | TERM
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_binary_expression(p):
    """
    BINARY_EXPRESSION : EXPRESSION '+' EXPRESSION
                      | EXPRESSION '-' EXPRESSION
                      | EXPRESSION '*' EXPRESSION
                      | EXPRESSION '/' EXPRESSION
    """
    p[0] = BinaryExpression(left=p[1], operation=p[2], right=p[3])


def p_logical_expression(p):
    """
    LOGICAL_EXPRESSION : EXPRESSION '>' EXPRESSION
                      | EXPRESSION '<' EXPRESSION
                      | EXPRESSION EQORGT EXPRESSION
                      | EXPRESSION EQORLESS EXPRESSION
                      | EXPRESSION EQUAL EXPRESSION
                      | EXPRESSION NOTEQUAL EXPRESSION
    """
    p[0] = LogicalExpression(left=p[1], operation=p[2], right=p[3])


def p_matrix_expression(p):
    """
    MATRIX_EXPRESSION : EXPRESSION DOTADD EXPRESSION
                      | EXPRESSION DOTSUB EXPRESSION
                      | EXPRESSION DOTMUL EXPRESSION
                      | EXPRESSION DOTDIV EXPRESSION
    """
    p[0] = MatrixExpression(left=p[1], operation=p[2], right=p[3])


def p_term(p):
    """
    TERM : ID
         | INTNUM
         | FLOATNUM
         | STRING
         | MATRIX
         | FUNCTION_CALL
         | ID "'"
         | '-' ID
    """
    if len(p) == 3:
        p[0] = Variable(str(p[1]) + str(p[2]))
    elif p.slice[1].type == 'ID':
        p[0] = Variable(p[1])
    elif p.slice[1].type == 'INTNUM':
        p[0] = Constant(p[1])
    elif p.slice[1].type == 'FLOATNUM':
        p[0] = Constant(p[1])
    elif p.slice[1].type == 'STRING':
        p[0] = Constant(p[1])
    else:
        p[0] = p[1]

def p_return(p):
    """
    EXPRESSION : RETURN TERM
    """
    p[0] = Return(p[2])


def p_intnum_or_id(p):
    """
    INTNUM_OR_ID : INTNUM
                 | ID
    """
    if p.slice[1].type == 'INTNUM':
        p[0] = Constant(p[1])
    else:
        p[0] = Variable(p[1])



def p_matrix(p):
    """
    MATRIX : '[' VECTORS ']'
    """
    p[0] = Matrix(p[2])


def p_vectors(p):
    """
    VECTORS : VECTORS ';' VECTOR
            | VECTOR
    """
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_vector(p):
    """
    VECTOR : VECTOR ',' TERM
           | TERM
    """
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = Vector(values=[p[1]])


# Terms?
def p_function_call(p):
    """
    FUNCTION_CALL : FUNCTION_NAME '(' TERM ')'
    """
    p[0] = FunctionCall(name=p[1], param=p[3])


def p_function_name(p):
    """
    FUNCTION_NAME : ZEROS
                  | ONES
                  | EYE
    """
    p[0] = p[1]


def p_control_instruction(p):
    """
    CONTROL_INSTRUCTION : BREAK
                        | CONTINUE
                        | RETURN
                        | RETURN TERM
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + " " + str(p[2])


def p_print_call(p):
    """
    PRINT_CALL : PRINT PRINT_TERMS
    """
    p[0] = p[2]


def p_print_terms(p):
    """
    PRINT_TERMS : PRINT_TERMS ',' TERM
                | TERM
    """
    if len(p) == 4:
        p[0] = p[1] + PrintCall(values=[p[3]])
    else:
        p[0] = PrintCall(values=[p[1]])


def p_if_condition(p):
    """
    IF_CONDITION    : IF '(' LOGICAL_EXPRESSION ')' INSTRUCTION ELIF_STATEMENTS ELSE_STATEMENT
                    | IF '(' LOGICAL_EXPRESSION ')' '{' INSTRUCTIONS '}' ELIF_STATEMENTS ELSE_STATEMENT
    ELIF_STATEMENTS : ELSEIF '(' LOGICAL_EXPRESSION ')' INSTRUCTION ELIF_STATEMENTS
                    | ELSEIF '(' LOGICAL_EXPRESSION ')' '{' INSTRUCTIONS '}' ELIF_STATEMENTS
                    | ELSEIF '(' LOGICAL_EXPRESSION ')' INSTRUCTION
                    | ELSEIF '(' LOGICAL_EXPRESSION ')' '{' INSTRUCTIONS '}'
    ELSE_STATEMENT  : ELSE INSTRUCTION
                    | ELSE '{' INSTRUCTIONS '}'
                    |
    """
    if p.slice[0].type == 'IF_CONDITION':
        if len(p) == 8:
            p[0] = IfCondition(condition=p[3], instructions=[p[5]], elif_branches=p[6], else_branch=p[7])
        else:
            p[0] = IfCondition(condition=p[3], instructions=[p[6]], elif_branches=p[8], else_branch=p[9])
    elif p.slice[0].type == 'ELIF_STATEMENTS':
        if len(p) == 6:
            p[0] = ElseIfConditions(conditions=[ElseIfCondition(condition=p[3], instructions=p[5])])
        if len(p) == 7:
            p[0] = ElseIfConditions(conditions=[ElseIfCondition(condition=p[3], instructions=p[5])]) + p[6]
        if len(p) == 8:
            p[0] = ElseIfConditions(conditions=[ElseIfCondition(condition=p[3], instructions=p[6])])
        elif len(p) == 9:
            p[0] = ElseIfConditions(conditions=[ElseIfCondition(condition=p[3], instructions=p[5])]) + p[8]
    elif p.slice[0].type == 'ELSE_STATEMENT':
        if len(p) == 3:
            p[0] = p[2]
        elif len(p) == 5:
            p[0] = p[3]


def p_for_loop(p):
    """
    FOR_LOOP : FOR FOR_CONDITION '{' INSTRUCTIONS '}'
             | FOR FOR_CONDITION  INSTRUCTION
    """
    if len(p) == 6:
        p[0] = ForLoop(for_condition=p[2], instructions=p[4])
    else:
        p[0] = ForLoop(for_condition=p[2], instructions=p[3])


def p_for_condition(p):
    """
    FOR_CONDITION : TERM '=' INTNUM_OR_ID ':' INTNUM_OR_ID
    """
    p[0] = ForCondition(variable=p[1], variable_range_first=p[3], variable_range_last=p[5])


def p_while_loop(p):
    """
    WHILE_LOOP : WHILE '(' LOGICAL_EXPRESSION ')' '{' INSTRUCTIONS '}'
               | WHILE '(' LOGICAL_EXPRESSION ')' INSTRUCTION
    """
    if len(p) == 8:
        p[0] = WhileLoop(condition=p[3], instructions=p[6])
    else:
        p[0] = WhileLoop(condition=p[3], instructions=p[5])


parser = yacc.yacc()
file = open(sys.argv[1], "r")
text = file.read()
scanner.lexer.input(text)

for token in scanner.lexer:
    print("%d: %s(%s)" % (token.lineno, token.type, token.value))

aaa = parser.parse(text, lexer=scanner.lexer)
print("----")
print(aaa)
