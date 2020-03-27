import scanner
import ply.yacc as yacc


tokens = scanner.tokens

for token in tokens:
    print(token)

precedence = (
   ("left", '+', '-'),
   ("left", '*', '/') )

def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, scanner.find_tok_column(p), p.type, p.value))
    else:
        print("Unexpected end of input")

def p_start(p):
    """start : EXPRESSION"""
    print("p[1]=", p[1])

def p_expression_number(p):
    """EXPRESSION : INTNUM"""
    p[0] = p[1]

def p_expression_string(p):
    """EXPRESSION : STRING"""
    p[0] = p[1]


def p_expression_sum(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION"""
    if   p[2]=='+': p[0] = p[1] + p[3];
    elif p[2]=='-': p[0] = p[1] - p[3];


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION"""
    if   p[2]=='*': p[0] = p[1] * p[3];
    elif p[2]=='/': p[0] = p[1] / p[3];


def p_expression_group(p):
    """EXPRESSION : '(' EXPRESSION ')'"""
    p[0] = p[2]

    


parser = yacc.yacc()