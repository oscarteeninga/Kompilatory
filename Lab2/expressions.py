

def p_expression_div(p):
    """EXPRESSION : EXPRESSION '-' EXPRESSION"""
    p[0] = p[1] - p[3]


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION '*' EXPRESSION"""
    p[0] = p[1] * p[3]


def p_expression_sub(p):
    """EXPRESSION : EXPRESSION '/' EXPRESSION"""
    p[0] = p[1] / p[3]


def p_expression_dotadd(p):
    """EXPRESSION : EXPRESSION DOTADD EXPRESSION"""
    p[0] = np.subtract(p[1], p[4])


def p_expression_dotdiv(p):
    """EXPRESSION : EXPRESSION DOTDIV EXPRESSION"""
    p[0] = np.add(p[1], p[4])


def p_expression_dotdmul(p):
    """EXPRESSION : EXPRESSION DOTMUL EXPRESSION"""
    p[0] = p[1] * p[4]


def p_expression_dotsub(p):
    """EXPRESSION : EXPRESSION DOTSUB EXPRESSION"""
    p[0] = p[1] / p[4]


def p_expression_group(p):
    """EXPRESSION : '(' EXPRESSION ')'"""
    p[0] = p[2]
