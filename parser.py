import ply.yacc as yacc
from lexer import tokens

pilaVariables = []
pilaVariables1 =[]
pilaTipos = []
pilaOperadores = []
pilaV = [[], []]

precedence = (
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
 )

def p_programa(p):
    '''programa : PROGRAMA ID SEMICOLON variables function principal'''

def p_principal(p):
    '''principal : PRINCIPAL LPAREN RPAREN bloque'''

def p_variables(p):
    '''variables : VARS variables1'''

def p_variables1(p):
    '''variables1 : INT COLON listaidsInt
                | FLOAT COLON listaidsFloat
                | CHAR COLON listaidsChar
                | '''

def p_listaidsInt(p):
    '''listaidsInt : ids COMA listaidsInt
                | ids SEMICOLON variables1
                | ids variables1'''
    pilaTipos.append('int')

def p_listaidsFloat(p):
    '''listaidsFloat : ids COMA listaidsFloat
                | ids SEMICOLON variables1
                | ids variables1'''
    pilaTipos.append('float')

def p_listaidsChar(p):
    '''listaidsChar : ids COMA listaidsChar
                | ids SEMICOLON variables1
                | ids variables1'''
    pilaTipos.append('char')

def p_ids(p):
    '''ids : ID'''
    pilaVariables.append(p[1])

def p_function(p):
    '''function : FUNCTION INT ID LPAREN variables1 RPAREN variables bloque
                | FUNCTION FLOAT ID LPAREN variables1 RPAREN variables bloque
                | FUNCTION INT ID LPAREN variables1 RPAREN variables bloque function
                | FUNCTION FLOAT ID LPAREN variables1 RPAREN variables bloque function'''
    pilaTipos.append(p[2])
    pilaVariables.append(p[3])

def p_bloque(p):
    '''bloque : LCBRACKET estatuto RCBRACKET
            | LCBRACKET RCBRACKET'''

def p_estatuto(p):
    '''estatuto : asignacion
                | retornofuncion
                | lectura
                | escritura
                | decision
                | repeticion'''
    #estatuto :lfvoid

def p_expresion(p): 
    '''expresion : expresion PLUS expresion
                | expresion MINUS expresion
                | expresion TIMES expresion
                | expresion DIVIDE expresion
                | expresion GTHAN expresion
                | expresion LTHAN expresion
                | LPAREN expresion RPAREN
                | INT
                | FLOAT
                | ARREGLO
                | ID'''
                #| ID LBRACKET INT RBRACKET expresion

def p_asignacion(p):
    '''asignacion : ID EQUALS expresion SEMICOLON estatuto
                | ID EQUALS expresion SEMICOLON
                | ARREGLO EQUALS expresion SEMICOLON estatuto
                | ARREGLO EQUALS expresion SEMICOLON'''
    a = 0
    for x in pilaVariables:
        if p[1] == pilaVariables[a]:
            break
        elif p[1] != pilaVariables[a]:
            if a == len(pilaVariables) - 1:
                p_error(p[1])    
        a = a + 1

def p_retornofuncion(p):
    '''retornofuncion : RETURN LPAREN expresion RPAREN SEMICOLON'''

def p_lectura(p):
    'lectura : READ LPAREN lectura1'

def p_lectura1(p):
    #Cambiar listaids
    '''lectura1 : listaidsInt SEMICOLON estatuto
                | listaidsInt SEMICOLON
                | RPAREN SEMICOLON estatuto
                | RPAREN SEMICOLON'''

def p_escritura(p):
    '''escritura : WRITE LPAREN escritura1 RPAREN SEMICOLON estatuto
                | WRITE LPAREN escritura1 RPAREN SEMICOLON'''

def p_escritura1(p):
    '''escritura1 : letrero 
                | letrero COMA escritura1
                | expresion
                | expresion COMA escritura1'''

def p_letrero(p):
    '''letrero : QUOTES ID QUOTES
            | COMA escritura1'''

def p_decision(p):
    '''decision : IF LPAREN opcion RPAREN THEN bloque estatuto
                | IF LPAREN opcion RPAREN THEN bloque
                | IF LPAREN opcion RPAREN THEN bloque decision1'''

def p_decision1(p):
    '''decision1 : ELSE bloque
                | ELSE bloque estatuto''' #falta el hacer nada

def p_opcion(p):
    '''opcion : expresion EQUALSDOBLE expresion
            | expresion'''

def p_repeticion(p):
    '''repeticion : condicional
                | nocondicional'''

def p_condicional(p):
    '''condicional :  WHILE LPAREN expresion RPAREN DO bloque
                | WHILE LPAREN expresion RPAREN DO bloque estatuto'''

def p_nocondicional(p):
    '''nocondicional : FOR ID EQUALS expresion TO expresion DO bloque
                    | FOR ID EQUALS expresion TO expresion DO bloque estatuto'''

def p_error(p):
    print("Syntax error in input!")
    
    print(p)

parser = yacc.yacc()

f = open("ejemplo.txt", "r")

while True:
    try:
        s = f.read()
    except EOFError:
        break
    if not s: break
    parser.parse(s)
    print(pilaVariables)
    print(pilaTipos)

f.close()