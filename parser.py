import ply.yacc as yacc
from lexer import tokens

precedence = (
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
 )

def p_programa(p):
    '''programa : PROGRAMA ID SEMICOLON variables function'''

def p_variables(p):
    '''variables : VARS variables1'''
    #'variables : VARS tipo COLON ID listaids | VARS tipo COLON ID LBRACKET INT RBRACKET listaids'

def p_variables1(p):
    'variables1 : tipo COLON listaids'

def p_listaids(p):
    'listaids : ID listaids1'

def p_listaids1(p):
    '''listaids1 : COMA ID listaids1
                | listaids2
                | SEMICOLON variables1
                | SEMICOLON
                | RPAREN'''

def p_listaids2(p):
    '''listaids2 : LBRACKET INT RBRACKET listaids1'''

def p_function(p):
    '''function : FUNCTION tiporetorno ID LPAREN variables1 variables bloque'''

def p_bloque(p):
    '''bloque : LCBRACKET estatuto
            | LCBRACKET RCBRACKET'''

#def p_bloque1(p):
#    '''bloque1 : RCBRACKET
#                | estatuto'''

def p_estatuto(p):
    '''estatuto : asignacion
                | retornofuncion
                | lectura
                | escritura
                | decision
                | repeticion
                | RBRACKET'''
    #estatuto :lfvoid

def p_asignacion(p):
    '''asignacion : ID EQUALS expresion SEMICOLON estatuto
                | ID LBRACKET expresion RBRACKET EQUALS expresion SEMICOLON estatuto'''

def p_retornofuncion(p):
    '''retornofuncion : RETURN LPAREN expresion RPAREN SEMICOLON'''

def p_expresion(p): 
    '''expresion : expresion PLUS expresion
                | expresion MINUS expresion
                | expresion TIMES expresion
                | expresion DIVIDE expresion
                | LPAREN expresion RPAREN
                | INT
                | FLOAT
                | ID'''

def p_lectura(p):
    'lectura : READ LPAREN lectura1'

def p_lectura1(p):
    '''lectura1 : RPAREN SEMICOLON
                | listaids lectura1'''

def p_escritura(p):
    'escritura : WRITE LPAREN escritura1'

def p_escritura1(p):
    '''escritura1 : letrero escritura2
                | expresion escritura2'''

def p_escritura2(p):
    '''escritura2 : RPAREN SEMICOLON
                | escritura1'''

def p_letrero(p):
    'letrero : QUOTES letrero1'

def p_letrero1(p):
    '''letrero1 : CHAR QUOTES
                | CHAR letrero1'''

def p_repeticion(p):
    '''repeticion : condicional
                | nocondicional'''

def p_decision(p):
    '''decision : IF LPAREN expresion RPAREN THEN bloque decision1'''

def p_decision1(p):
    '''decision1 : ELSE bloque''' #falta el hacer nada

def p_condicional(p):
    '''condicional : WHILE LPAREN expresion RPAREN DO bloque'''

def p_nocondicional(p):
    '''nocondicional : FOR ID EQUALS expresion TO expresion DO bloque'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR'''

def p_tiporetorno(p):
    '''tiporetorno : INT
                | FLOAT''' #or void

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

f = open("ejemplo.txt", "r")

while True:
    try:
        s = f.read()
    except EOFError:
        break
    if not s: break
    result = parser.parse(s)
    print(result)

f.close()