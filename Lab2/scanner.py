import sys
import ply.lex as lex

tokens = ('ADDASSIGN', 'SUBASSIGN','MULASSIGN', 'DIVASSIGN',
            'EQORGT', 'EQORLESS', 'EQUAL', 'NOTEQUAL',
            'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 
            'ZEROS','ONES','EYE',
            'INTNUM', 'FLOATNUM', 'STRING',
            'IF', 'ELSE', 'FOR', 'WHILE', 
            'BREAK', 'CONTINUE', 'RETURN',
            'PRINT', 'ID')

t_ignore = '  \t'
t_EQORGT = r'\>\='
t_EQORLESS = r'\<\='
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_ADDASSIGN = r'\+\='
t_SUBASSIGN = r'\-\='
t_MULASSIGN = r'\*\='
t_DIVASSIGN = r'\/\='
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.\-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\.\/'

literals = [ '+','-','*','/','(',')','[',']','{','}','=',',',';','\'', '<', '>']

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_error(t) :
    print ("Illegal character %s" %t.value[0])
    t.lexer.skip(1)

def t_FLOATNUM(t):
    r"""
        [+-]?            # optional sign
        (?:              # start non-capture group
          \d+?\.\d+      # a.b
          |              # or
          \.\d+          # .b
          |              # or
          \d+?\.         # a.
        )                #
        (?:              # start non-capture group
          [eE][+-]?\d+   # match exponent
        )?               # optionally
    """
    t.value = float(t.value)
    return t

def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'("[^"]*")'
    return t

def t_ZEROS(t):
    r'zeros'
    return t

def t_ONES(t):
    r'ones'
    return t

def t_EYE(t):
    r'eye'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

lexer = lex.lex()
fh = open("example1.m", "r")
lexer.input( fh.read() )

for token in lexer:
    print("%d: %s(%s)" %(token.lineno, token.type, token.value))