import ply.lex as lex

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'to' : 'TO',
    'do' : 'DO',
    'for' : 'FOR',
    'return' : 'RETURN',
    'programa' : 'PROGRAMA',
    'vars' : 'VARS',
    'function' : 'FUNCTION',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'read' : 'READ',
    'write' : 'WRITE',
    'int' : 'INT',
    'void' : 'VOID',
    'arreglo' : 'ARREGLO',
    'principal' : 'PRINCIPAL'
}

tokens = [
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'GTHAN',
    'LTHAN',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'RBRACKET',
    'LBRACKET',
    'LCBRACKET',
    'RCBRACKET',
    'SQUOTES',
    'COLON',
    'SEMICOLON',
    'COMA',
    'DOT',
    'OR',
    'QUOTES',
    'AND',
    'EQUALSDOBLE',
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GTHAN = r'\>'
t_LTHAN = r'\<'
t_EQUALSDOBLE = r'\=\='
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_SQUOTES = r'\''
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMA = r'\,'
t_DOT = r'\.'
t_OR = r'\|'
t_QUOTES = r'\"'
t_AND = r'\&'

def t_INTP(t):
    r'int'
    t.type = reserved.get(t.value,'INT')
    return t

def t_PROGRAMA(t):
    r'programa | PROGRAMA'
    t.type = reserved.get(t.value,'PROGRAMA')
    return t

def t_PRINCIPAL(t):
    r'principal | PRINCIPAL'
    t.type = reserved.get(t.value,'PRINCIPAL')
    return t

def t_VARS(t):
    r'VARS | vars'
    t.type = reserved.get(t.value,'VARS')
    return t

def t_VOID(t):
    r'VOID | void'
    t.type = reserved.get(t.value,'VOID')
    return t

def t_IF(t):
    r'if'
    t.type = reserved.get(t.value,'IF')
    return t

def t_THEN(t):
    r'then'
    t.type = reserved.get(t.value,'THEN')
    return t

def t_WHILE(t):
    r'while'
    t.type = reserved.get(t.value,'WHILE')
    return t

def t_READ(t):
    r'read'
    t.type = reserved.get(t.value,'READ')
    return t

def t_WRITE(t):
    r'write'
    t.type = reserved.get(t.value,'WRITE')
    return t

def t_ELSE(t):
    r'else'
    t.type = reserved.get(t.value,'ELSE')
    return t

def t_TO(t):
    r'to'
    t.type = reserved.get(t.value,'TO')
    return t

def t_DO(t):
    r'do'
    t.type = reserved.get(t.value,'DO')
    return t

def t_FOR(t):
    r'for'
    t.type = reserved.get(t.value,'FOR')
    return t

def t_RETURN(t):
    r'return'
    t.type = reserved.get(t.value,'RETURN')
    return t

def t_FUNCTION(t):
    r'function'
    t.type = reserved.get(t.value,'FUNCTION')
    return t

def t_CHARP(t):
    r'char'
    t.type = reserved.get(t.value,'CHAR')
    return t

def t_FLOATP(t):
    r'float'
    t.type = reserved.get(t.value,'FLOAT')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d'
    t.value = float(t.value)
    return t

def t_ARREGLO(t):
     r'[a-zA-Z]([a-zA-Z] | \d+)*\[\d+\]'
     t.type = reserved.get(t.value,'ARREGLO')
     return t

def t_ID(t):
     r'[a-zA-Z]([a-zA-Z] | \d+)*'
     t.type = reserved.get(t.value,'ID')
     return t
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

lexer = lex.lex()

f = open("completo.txt", "r")
data = f.read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break     
    print(tok)