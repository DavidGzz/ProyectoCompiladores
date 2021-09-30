import ply.yacc as yacc
from lexer import tokens

precedence = (
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
 )

def p_programa(p):
    'programa : programa id ; vars function bloque'

def p_vars(p):
    'vars : vars tipo : listaids ;'

def p_tipo(p):
    'tipo : int | float | char'

def p_listaids(p):
    'listaids : id listaids1 | id [ int ] listaids1 ;'

def p_listaids1(p):
    'listaids1 : , listaids | ;'

def p_function(p):
    'function : function tiporetorno id ( parametros ) ; vars bloque'

def p_bloque(p):
    'bloque : LCBRACKET estatuto bloque1 | LCBRACKET RCBRACKET'

def p_bloque1(p):
    'bloque1 : RCBRACKET | estatuto '

def p_estatuto(p):
    'estatuto : asignacion | lfvoid | retornofuncion | lectura | escritura | decision | repeticion'

def p_tiporetorno(p):
    'tiporetorno : int | float | eps'

def p_asignacion(p):
    'asignacion : id EQUALS expresion ; | id LBRACKET exp RBRACKET EQUALS expresion ;'

def p_retornofuncion(p):
    'retornofuncion : return LPAREN exp RPAREN ;'

def p_lectura(p):
    'lectura : read LPAREN lectura1'

def p_lectura1(p):
    'lectura1 : RPAREN ; | listaids lectura1'

def p_escritura(p):
    'escritura : write LPAREN escritura1'

def p_escritura1(p):
    'escritura1 : letrero escritura2 | expresion escritura2'

def p_escritura2(p):
    'escritura2 : RPAREN ; | escriutra1'

def p_letrero(p):
    'letrero : " char '

parser = yacc.yacc()