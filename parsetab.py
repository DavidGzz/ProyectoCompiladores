
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEAND CHAR COLON COMA DIVIDE DO DOT ELSE EQUALS FLOAT FOR FUNCTION GTHAN ID IF INT LBRACKET LCBRACKET LPAREN LTHAN MINUS OR PLUS PROGRAMA QUOTES RBRACKET RCBRACKET READ RETURN RPAREN SEMICOLON SQUOTES THEN TIMES TO VARS WHILE WRITEprograma : PROGRAMA ID SEMICOLON variables functionvariables : VARS variables1variables1 : tipo COLON listaidslistaids : ID listaids1listaids1 : COMA ID listaids1\n                | listaids2\n                | SEMICOLON variables1\n                | SEMICOLON\n                | RPARENlistaids2 : LBRACKET INT RBRACKET listaids1function : FUNCTION tiporetorno ID LPAREN variables1 variables bloquebloque : LCBRACKET estatuto\n            | LCBRACKET RCBRACKETestatuto : asignacion\n                | retornofuncion\n                | lectura\n                | escritura\n                | decision\n                | repeticion\n                | RBRACKETasignacion : ID EQUALS expresion SEMICOLON estatuto\n                | ID LBRACKET expresion RBRACKET EQUALS expresion SEMICOLON estatutoretornofuncion : RETURN LPAREN expresion RPAREN SEMICOLONexpresion : expresion PLUS expresion\n                | expresion MINUS expresion\n                | expresion TIMES expresion\n                | expresion DIVIDE expresion\n                | LPAREN expresion RPAREN\n                | INT\n                | FLOAT\n                | IDlectura : READ LPAREN lectura1lectura1 : RPAREN SEMICOLON\n                | listaids lectura1escritura : WRITE LPAREN escritura1escritura1 : letrero escritura2\n                | expresion escritura2escritura2 : RPAREN SEMICOLON\n                | escritura1letrero : QUOTES letrero1letrero1 : CHAR QUOTES\n                | CHAR letrero1repeticion : condicional\n                | nocondicionaldecision : IF LPAREN expresion RPAREN THEN bloque decision1decision1 : ELSE bloquecondicional : WHILE LPAREN expresion RPAREN DO bloquenocondicional : FOR ID EQUALS expresion TO expresion DO bloquetipo : INT\n            | FLOAT\n            | CHARtiporetorno : INT\n                | FLOAT'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,7,35,38,39,40,41,42,43,44,45,46,52,53,71,74,89,90,91,93,94,100,107,108,116,119,122,123,124,],[0,-1,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-43,-44,-32,-35,-33,-34,-36,-39,-37,-21,-23,-38,-47,-45,-22,-46,-48,]),'ID':([2,14,15,16,17,19,22,23,24,25,26,30,33,36,37,55,56,57,58,59,60,61,62,64,66,67,68,73,75,76,80,81,82,83,84,85,95,101,102,103,104,105,106,109,110,113,118,],[3,18,-52,-53,20,-3,-4,29,-6,-8,-9,-7,-5,47,-10,63,64,64,64,20,64,64,64,-31,64,-29,-30,20,64,64,64,47,64,64,64,64,-40,-24,-25,-26,-27,-28,64,-41,-42,64,47,]),'SEMICOLON':([3,20,29,34,64,65,67,68,72,88,92,101,102,103,104,105,114,],[4,25,25,25,-31,81,-29,-30,89,107,108,-24,-25,-26,-27,-28,118,]),'VARS':([4,19,22,24,25,26,28,30,33,37,],[6,-3,-4,-6,-8,-9,6,-7,-5,-10,]),'FUNCTION':([5,9,19,22,24,25,26,30,33,37,],[8,-2,-3,-4,-6,-8,-9,-7,-5,-10,]),'INT':([6,8,21,25,27,56,57,58,60,61,62,64,66,67,68,75,76,80,82,83,84,85,95,101,102,103,104,105,106,109,110,113,],[11,15,11,11,31,67,67,67,67,67,67,-31,67,-29,-30,67,67,67,67,67,67,67,-40,-24,-25,-26,-27,-28,67,-41,-42,67,]),'FLOAT':([6,8,21,25,56,57,58,60,61,62,64,66,67,68,75,76,80,82,83,84,85,95,101,102,103,104,105,106,109,110,113,],[12,16,12,12,68,68,68,68,68,68,-31,68,-29,-30,68,68,68,68,68,68,68,-40,-24,-25,-26,-27,-28,68,-41,-42,68,]),'CHAR':([6,21,25,77,96,],[13,13,13,96,96,]),'LCBRACKET':([9,19,22,24,25,26,30,32,33,37,111,112,120,121,],[-2,-3,-4,-6,-8,-9,-7,36,-5,-10,36,36,36,36,]),'COLON':([10,11,12,13,],[17,-49,-50,-51,]),'LPAREN':([18,48,49,50,51,54,56,57,58,60,61,62,64,66,67,68,75,76,80,82,83,84,85,95,101,102,103,104,105,106,109,110,113,],[21,58,59,60,61,62,66,66,66,66,66,66,-31,66,-29,-30,66,66,66,66,66,66,66,-40,-24,-25,-26,-27,-28,66,-41,-42,66,]),'RPAREN':([19,20,22,24,25,26,29,30,33,34,37,59,64,67,68,70,73,75,76,78,79,86,95,101,102,103,104,105,109,110,],[-3,26,-4,-6,-8,-9,26,-7,-5,26,-10,72,-31,-29,-30,88,72,92,92,97,98,105,-40,-24,-25,-26,-27,-28,-41,-42,]),'COMA':([20,29,34,],[23,23,23,]),'LBRACKET':([20,29,34,47,],[27,27,27,57,]),'RBRACKET':([31,36,64,67,68,69,81,101,102,103,104,105,118,],[34,46,-31,-29,-30,87,46,-24,-25,-26,-27,-28,46,]),'RCBRACKET':([36,],[39,]),'RETURN':([36,81,118,],[48,48,48,]),'READ':([36,81,118,],[49,49,49,]),'WRITE':([36,81,118,],[50,50,50,]),'IF':([36,81,118,],[51,51,51,]),'WHILE':([36,81,118,],[54,54,54,]),'FOR':([36,81,118,],[55,55,55,]),'ELSE':([38,39,40,41,42,43,44,45,46,52,53,71,74,89,90,91,93,94,100,107,108,115,116,119,122,123,124,],[-12,-13,-14,-15,-16,-17,-18,-19,-20,-43,-44,-32,-35,-33,-34,-36,-39,-37,-21,-23,-38,120,-47,-45,-22,-46,-48,]),'EQUALS':([47,63,87,],[56,80,106,]),'QUOTES':([60,64,67,68,75,76,95,96,101,102,103,104,105,109,110,],[77,-31,-29,-30,77,77,-40,109,-24,-25,-26,-27,-28,-41,-42,]),'PLUS':([64,65,67,68,69,70,76,78,79,86,99,101,102,103,104,105,114,117,],[-31,82,-29,-30,82,82,82,82,82,82,82,-24,-25,-26,-27,-28,82,82,]),'MINUS':([64,65,67,68,69,70,76,78,79,86,99,101,102,103,104,105,114,117,],[-31,83,-29,-30,83,83,83,83,83,83,83,-24,-25,-26,-27,-28,83,83,]),'TIMES':([64,65,67,68,69,70,76,78,79,86,99,101,102,103,104,105,114,117,],[-31,84,-29,-30,84,84,84,84,84,84,84,84,84,-26,-27,-28,84,84,]),'DIVIDE':([64,65,67,68,69,70,76,78,79,86,99,101,102,103,104,105,114,117,],[-31,85,-29,-30,85,85,85,85,85,85,85,85,85,-26,-27,-28,85,85,]),'TO':([64,67,68,99,101,102,103,104,105,],[-31,-29,-30,113,-24,-25,-26,-27,-28,]),'DO':([64,67,68,98,101,102,103,104,105,117,],[-31,-29,-30,112,-24,-25,-26,-27,-28,121,]),'THEN':([97,],[111,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'variables':([4,28,],[5,32,]),'function':([5,],[7,]),'variables1':([6,21,25,],[9,28,30,]),'tipo':([6,21,25,],[10,10,10,]),'tiporetorno':([8,],[14,]),'listaids':([17,59,73,],[19,73,73,]),'listaids1':([20,29,34,],[22,33,37,]),'listaids2':([20,29,34,],[24,24,24,]),'bloque':([32,111,112,120,121,],[35,115,116,123,124,]),'estatuto':([36,81,118,],[38,100,122,]),'asignacion':([36,81,118,],[40,40,40,]),'retornofuncion':([36,81,118,],[41,41,41,]),'lectura':([36,81,118,],[42,42,42,]),'escritura':([36,81,118,],[43,43,43,]),'decision':([36,81,118,],[44,44,44,]),'repeticion':([36,81,118,],[45,45,45,]),'condicional':([36,81,118,],[52,52,52,]),'nocondicional':([36,81,118,],[53,53,53,]),'expresion':([56,57,58,60,61,62,66,75,76,80,82,83,84,85,106,113,],[65,69,70,76,78,79,86,76,76,99,101,102,103,104,114,117,]),'lectura1':([59,73,],[71,90,]),'escritura1':([60,75,76,],[74,93,93,]),'letrero':([60,75,76,],[75,75,75,]),'escritura2':([75,76,],[91,94,]),'letrero1':([77,96,],[95,110,]),'decision1':([115,],[119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAMA ID SEMICOLON variables function','programa',5,'p_programa','parser.py',10),
  ('variables -> VARS variables1','variables',2,'p_variables','parser.py',13),
  ('variables1 -> tipo COLON listaids','variables1',3,'p_variables1','parser.py',17),
  ('listaids -> ID listaids1','listaids',2,'p_listaids','parser.py',20),
  ('listaids1 -> COMA ID listaids1','listaids1',3,'p_listaids1','parser.py',23),
  ('listaids1 -> listaids2','listaids1',1,'p_listaids1','parser.py',24),
  ('listaids1 -> SEMICOLON variables1','listaids1',2,'p_listaids1','parser.py',25),
  ('listaids1 -> SEMICOLON','listaids1',1,'p_listaids1','parser.py',26),
  ('listaids1 -> RPAREN','listaids1',1,'p_listaids1','parser.py',27),
  ('listaids2 -> LBRACKET INT RBRACKET listaids1','listaids2',4,'p_listaids2','parser.py',30),
  ('function -> FUNCTION tiporetorno ID LPAREN variables1 variables bloque','function',7,'p_function','parser.py',33),
  ('bloque -> LCBRACKET estatuto','bloque',2,'p_bloque','parser.py',36),
  ('bloque -> LCBRACKET RCBRACKET','bloque',2,'p_bloque','parser.py',37),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',44),
  ('estatuto -> retornofuncion','estatuto',1,'p_estatuto','parser.py',45),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','parser.py',46),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','parser.py',47),
  ('estatuto -> decision','estatuto',1,'p_estatuto','parser.py',48),
  ('estatuto -> repeticion','estatuto',1,'p_estatuto','parser.py',49),
  ('estatuto -> RBRACKET','estatuto',1,'p_estatuto','parser.py',50),
  ('asignacion -> ID EQUALS expresion SEMICOLON estatuto','asignacion',5,'p_asignacion','parser.py',54),
  ('asignacion -> ID LBRACKET expresion RBRACKET EQUALS expresion SEMICOLON estatuto','asignacion',8,'p_asignacion','parser.py',55),
  ('retornofuncion -> RETURN LPAREN expresion RPAREN SEMICOLON','retornofuncion',5,'p_retornofuncion','parser.py',58),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion','parser.py',61),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion','parser.py',62),
  ('expresion -> expresion TIMES expresion','expresion',3,'p_expresion','parser.py',63),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion','parser.py',64),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_expresion','parser.py',65),
  ('expresion -> INT','expresion',1,'p_expresion','parser.py',66),
  ('expresion -> FLOAT','expresion',1,'p_expresion','parser.py',67),
  ('expresion -> ID','expresion',1,'p_expresion','parser.py',68),
  ('lectura -> READ LPAREN lectura1','lectura',3,'p_lectura','parser.py',71),
  ('lectura1 -> RPAREN SEMICOLON','lectura1',2,'p_lectura1','parser.py',74),
  ('lectura1 -> listaids lectura1','lectura1',2,'p_lectura1','parser.py',75),
  ('escritura -> WRITE LPAREN escritura1','escritura',3,'p_escritura','parser.py',78),
  ('escritura1 -> letrero escritura2','escritura1',2,'p_escritura1','parser.py',81),
  ('escritura1 -> expresion escritura2','escritura1',2,'p_escritura1','parser.py',82),
  ('escritura2 -> RPAREN SEMICOLON','escritura2',2,'p_escritura2','parser.py',85),
  ('escritura2 -> escritura1','escritura2',1,'p_escritura2','parser.py',86),
  ('letrero -> QUOTES letrero1','letrero',2,'p_letrero','parser.py',89),
  ('letrero1 -> CHAR QUOTES','letrero1',2,'p_letrero1','parser.py',92),
  ('letrero1 -> CHAR letrero1','letrero1',2,'p_letrero1','parser.py',93),
  ('repeticion -> condicional','repeticion',1,'p_repeticion','parser.py',96),
  ('repeticion -> nocondicional','repeticion',1,'p_repeticion','parser.py',97),
  ('decision -> IF LPAREN expresion RPAREN THEN bloque decision1','decision',7,'p_decision','parser.py',100),
  ('decision1 -> ELSE bloque','decision1',2,'p_decision1','parser.py',103),
  ('condicional -> WHILE LPAREN expresion RPAREN DO bloque','condicional',6,'p_condicional','parser.py',106),
  ('nocondicional -> FOR ID EQUALS expresion TO expresion DO bloque','nocondicional',8,'p_nocondicional','parser.py',109),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',112),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',113),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',114),
  ('tiporetorno -> INT','tiporetorno',1,'p_tiporetorno','parser.py',117),
  ('tiporetorno -> FLOAT','tiporetorno',1,'p_tiporetorno','parser.py',118),
]
