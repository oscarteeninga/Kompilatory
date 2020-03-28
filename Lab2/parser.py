import scanner
import ply.yacc as yacc
import numpy as np
import math
import sys

import attr


class Node:
    pass


@attr.s
class IfCondition(Node):
    condition = attr.ib()
    instruction = attr.ib()
    else_branch = attr.ib(default=None)


names = {}

tokens = scanner.tokens

precedence = ()


def p_error(p):
    if p:
        print("Syntax error at line {0}, LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_expression_statement(p):
    """EXPRESSION : TERM
                  | EXPRESSION TERM
                  | EXPRESSION IF_CONDITION"""
    p[0] = p[1]


def p_term(p):
    """TERM : STATEMENT
            | PRINT"""
    p[0] = p[1]


def p_var(p):
    """VAR : NUM
           | MATRIX"""
    p[0] = p[1]


def p_num(p):
    """NUM : INTNUM
           | FLOATNUM"""
    p[0] = p[1]


def p_vector(p):
    """VECTOR : VECTOR ',' NUM
              | NUM"""
    if len(p) > 2:
        p[0] = np.append(p[1], p[3])
    else:
        p[0] = [p[1]]


def p_vectors(p):
    """VECTORS : VECTORS ';' VECTOR
               | VECTOR"""
    if len(p) > 2:
        p[0] = np.append(p[1], p[3])
    else:
        p[0] = [p[1]]


def p_matrix(p):
    """MATRIX : '[' VECTORS ']'"""
    N = int(math.sqrt(len(p[2])))
    MATRIX = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            i = int(i)
            j = int(j)
            MATRIX[i][j] = p[2][i * 3 + j]
    p[0] = MATRIX


def p_zeros(p):
    """MATRIX : ZEROS '(' INTNUM ')'"""
    p[0] = np.zeros((p[3], p[3]))


def p_ones(p):
    """MATRIX : ONES '(' INTNUM ')'"""
    p[0] = np.ones((p[3], p[3]))


def p_eye(p):
    """MATRIX : EYE '(' INTNUM ')'"""
    p[0] = np.eye(N=p[3], M=p[3])


def p_matrix_min(p):
    """MATRIX : '-' ID"""
    p[0] = -names[p[2]]


def p_matrix_trans(p):
    """MATRIX : ID '\\''"""
    p[0] = names[p[1]].transpose()


def p_sum(p):
    """VAR : ID '+' ID"""
    p[0] = names[p[1]] + names[p[3]]


def p_sub(p):
    """VAR : ID '-' ID"""
    p[0] = names[p[1]] - names[p[3]]


def p_mul(p):
    """VAR : ID '*' ID"""
    p[0] = names[p[1]] * names[p[3]]


def p_div(p):
    """VAR : ID '/' ID"""
    p[0] = names[p[1]] / names[p[3]]


def p_dotadd(p):
    """MATRIX : ID DOTADD ID"""
    p[0] = np.add(names[p[1]], names[p[3]])


def p_dotsub(p):
    """MATRIX : ID DOTSUB ID"""
    p[0] = np.subtract(names[p[1]], names[p[3]])


def p_dotmul(p):
    """MATRIX : ID DOTMUL ID"""
    p[0] = np.matmul(names[p[1]], names[p[3]])


def p_dotdiv(p):
    """MATRIX : ID DOTDIV ID"""
    p[0] = np.divide(names[p[1]], names[p[3]])


def p_var_statement_assignment(p):
    """STATEMENT : ID '=' VAR ';'"""
    p[0] = p[3]
    names[p[1]] = p[3]


def p_matrix_element_assignment(p):
    """STATEMENT : ID '[' INTNUM ',' INTNUM ']' '=' NUM ';'"""
    names[p[1]][p[3]][p[5]] = p[8]


def p_addassign(p):
    """STATEMENT : ID ADDASSIGN ID ';'"""
    names[p[1]] = names[p[1]] + names[p[3]]


def p_subassign(p):
    """STATEMENT : ID SUBASSIGN ID ';'"""
    names[p[1]] = names[p[1]] - names[p[3]]


def p_mulassign(p):
    """STATEMENT : ID MULASSIGN ID ';'"""
    names[p[1]] = np.matmul(names[p[1]], names[p[3]])


def p_divassign(p):
    """STATEMENT : ID DIVASSIGN ID ';'"""
    names[p[1]] = np.divide(names[p[1]], names[p[3]])


def p_print_id(p):
    """TERM : PRINT '(' ID ')' ';'"""
    print(p[3], '=', names[p[3]])
    p[0] = names[p[3]]


def p_print_var(p):
    """TERM : PRINT '(' VAR ')' ';'"""
    print(p[3])
    p[0] = p[3]


def p_print_string(p):
    """TERM : PRINT '(' STRING ')' ';'"""
    print(p[3])
    p[0] = p[3]


def p_if_condition(p):
    """
    IF_CONDITION   : IF '(' LOGICAL_EXPRESSION ')' EXPRESSION ELSE_STATEMENT
    ELSE_STATEMENT : ELSE EXPRESSION
                   |
    """
    if p.slice[0].type == 'IF_CONDITION':
        if p[3]:
            p[0] = p[5]
        else:
            p[0] = p[6]
    elif len(p) == 3:
        p[0] = p[2]


def p_logical_expression(p):
    """LOGICAL_EXPRESSION : ID EQUAL INTNUM"""
    p[0] = (names[p[1]] == p[3])


parser = yacc.yacc()
file = open(sys.argv[1], "r")
text = file.read()
scanner.lexer.input(text)

for token in scanner.lexer:
    print("%d: %s(%s)" % (token.lineno, token.type, token.value))

aaa = parser.parse(text, lexer=scanner.lexer)
print("----")
print(aaa)
