import ply.yacc as yacc
from lexer import tokens

pilaVariables = []
pilaVariablesFunciones =[]
pilaTipos = []
pilaVariablesLocales = []
pilaOperadores = []
pilaFunciones = []
pilaTiposFunciones = []
pilaTiposLocales = []

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
    '''variables1 : tipo COLON listaids
                | '''

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR'''
    pilaTipos.append(p[1])

#def p_variables1(p):
#    '''variables1 : INT COLON listaidsInt
#                | FLOAT COLON listaidsFloat
#                | CHAR COLON listaidsChar
#                | '''

def p_listaids(p):
    '''listaids : ids COMA listaids
                | ids SEMICOLON variables1
                | ids variables1'''

def p_ids(p):
    '''ids : ID'''
    pilaVariables.append(p[1])

#def p_listaidsInt(p):
#    '''listaidsInt : ids COMA listaidsInt
#                | ids SEMICOLON variables1
#                | ids variables1'''
#    p_tipos('int')

#def p_listaidsFloat(p):
#    '''listaidsFloat : ids COMA listaidsFloat
#                | ids SEMICOLON variables1
#                | ids variables1'''
#    p_tipos('float')

#def p_listaidsChar(p):
#    '''listaidsChar : ids COMA listaidsChar
#                | ids SEMICOLON variables1
#                | ids variables1'''
#    p_tipos('char')

#def p_tipos(p):
#    pilaTipos.append(p)

#def p_ids(p):
#    '''ids : ID'''
#    pilaVariables.append(p[1])

def p_function(p):
    '''function : FUNCTION tiporetorno idsFu LPAREN variablesF RPAREN variablesL bloque
                | FUNCTION tiporetorno idsFu LPAREN variablesF RPAREN variablesL bloque function'''

def p_tiporetorno(p):
    '''tiporetorno : INT
                | FLOAT
                | VOID''' #or void
    pilaTiposFunciones.append(p[1])

def p_variablesF(p):
    '''variablesF : tipo COLON listaidsF'''

def p_listaidsF(p):
    '''listaidsF : idsF COMA listaidsF
                | idsF'''

def p_idsF(p):
    '''idsF : ID'''
    pilaVariablesFunciones.append(p[1])

def p_idsFu(p):
    '''idsFu : ID'''
    pilaFunciones.append(p[1])

def p_variablesL(p):
    '''variablesL : VARS variablesL1'''

def p_variablesL1(p):
    '''variablesL1 : tipoL COLON listaidsL
                    | '''

def p_tipoL(p):
    '''tipoL : INT
                | FLOAT
                | CHAR'''
    pilaTiposLocales.append(p[1])

def p_listaidsL(p):
    '''listaidsL : idsL COMA listaidsL
                | idsL SEMICOLON variablesL1
                | idsL variablesL1'''

def p_idsL(p):
    '''idsL : ID'''
    pilaVariablesLocales.append(p[1])

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

def p_retornofuncion(p):
    '''retornofuncion : RETURN LPAREN expresion RPAREN SEMICOLON'''

def p_lectura(p):
    'lectura : READ LPAREN lectura1'

def p_lectura1(p):
    #Cambiar listaids
    '''lectura1 : listaids SEMICOLON estatuto
                | listaids SEMICOLON
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
    print("V", pilaVariables)
    print("VL", pilaVariablesLocales)
    print("VF", pilaVariablesFunciones)
    print("T", pilaTipos)
    print("TL", pilaTiposLocales)
    print("TF", pilaTiposFunciones)
    print("PF", pilaFunciones)


f.close()