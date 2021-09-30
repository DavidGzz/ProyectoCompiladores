import ply.yacc as yacc
from lexer import tokens

precedence = (
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
 )

def p_programa(p):
    'programa : PROGRAMA ID SEMICOLON variables function bloque'

def p_variables(p):
    'variables : VARS variables1'
    #'variables : VARS tipo COLON ID listaids OR VARS tipo COLON ID LBRACKET INT RBRACKET listaids'

def p_variables1(p):
    'variables1 : tipo COLON listaids'

def p_listaids(p):
    'listaids : ID listaids1'

def p_listaids1(p):
    'listaids1 : COMA listaids1 OR listaids2'

def p_listaids2(p):
    'listaids2 : LBRACKET INT RBRACKET COMA listaids1 OR LBRACKET INT RBRACKET SEMICOLON OR SEMICOLON'

def p_tipo(p):
    'tipo : INT OR FLOAT OR CHAR'

def p_function(p):
    'function : function tiporetorno ID LPAREN parametros RPAREN SEMICOLON variables bloque'

def p_bloque(p):
    'bloque : LCBRACKET estatuto bloque1 OR LCBRACKET RCBRACKET'

def p_bloque1(p):
    'bloque1 : RCBRACKET OR estatuto'

def p_estatuto(p):
    'estatuto : asignacion OR retornofuncion OR lectura OR escritura'
    #'estatuto : asignacion OR lfvoid OR retornofuncion OR lectura OR escritura OR decision OR repeticion'

def p_tiporetorno(p):
    'tiporetorno : INT OR FLOAT OR 0' #or eps

def p_asignacion(p):
    'asignacion : ID EQUALS expresion SEMICOLON OR ID LBRACKET exp RBRACKET EQUALS expresion SEMICOLON'

def p_retornofuncion(p):
    'retornofuncion : RETURN LPAREN exp RPAREN SEMICOLON'

def p_expresion(p):
    'expresion : exp expresion1'

def p_expresion1(p):
    'expresion1 : GTHAN exp OR LTHAN exp' #<> exp

def p_exp(p):
    'exp : termino exp1'

def p_exp1(p):
    'exp1 : PLUS exp OR MINUS exp OR NONE' #or eps

def p_termino(p):
    'termino : factor termino1'

def p_termino1(p):
    'termino1 : TIMES termino OR DIVIDE termino OR NONE' #or eps

def p_factor(p):
    'factor : LCBRACKET expresion RCBRACKET'

def p_factor(p):
    'factor : PLUS varcte OR MINUS varcte OR varcte'

def p_varcte(p):
    'varcte : INT OR FLOAT OR ID'

#FACTOR -> + VAR CTE | - VAR CTE | VAR CTE
#VAR CTE -> cte l | cte f | id

def p_lectura(p):
    'lectura : READ LPAREN lectura1'

def p_lectura1(p):
    'lectura1 : RPAREN SEMICOLON OR listaids lectura1'

def p_escritura(p):
    'escritura : WRITE LPAREN escritura1'

def p_escritura1(p):
    'escritura1 : letrero escritura2 OR expresion escritura2'

def p_escritura2(p):
    'escritura2 : RPAREN SEMICOLON OR escriutra1'

def p_letrero(p):
    'letrero : QUOTES letrero1'

def p_letrero1(p):
    'letrero1 : CHAR QUOTES OR CHAR letrero1'

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()