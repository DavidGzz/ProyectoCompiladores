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
    'funcion' : 'FUNCION',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'read' : 'READ',
    'write' : 'WRITE',
}

tokens = [
    'NUMBER',
    'LETTER',
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
] + list(reserved.values())

t_ignore = ' \t'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GTHAN = r'\>'
t_LTHAN = r'\<'
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_RCBRACKET = r'\{'
t_LCBRACKET = r'\}'
t_SQUOTES = r'\''
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMA = r'\,'
t_DOT = r'\.'
t_OR = r'\|'
t_QUOTES = r'\"'

def t_LETTER(t):
    r'[a-zA-Z]'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
     r'LETTER(LETTER | NUMBER)*'
     t.type = reserved.get(t.value,'ID')
     return t
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

lexer = lex.lex()

 # Test it out
data = '''
if r > 5.5 then:
    return a;
'''
 
 # Give the lexer some input
lexer.input(data)
 
 # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)