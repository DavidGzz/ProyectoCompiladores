
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEAND CHAR COLON COMA DIVIDE DO DOT ELSE EMPTY EPS EQUALS FLOAT FOR FUNCTION GTHAN ID IF INT LBRACKET LCBRACKET LPAREN LTHAN MINUS OR PLUS PROGRAMA QUOTES RBRACKET RCBRACKET READ RETURN RPAREN SEMICOLON SQUOTES THEN TIMES TO VARS WHILE WRITEprograma : PROGRAMA ID SEMICOLON variables function bloquevariables : VARS variables1variables1 : tipo COLON listaidslistaids : ID listaids1listaids1 : COMA ID listaids1 \n                | listaids2 \n                | SEMICOLONlistaids2 : LBRACKET INT RBRACKET listaids1 \n                | LBRACKET INT RBRACKET SEMICOLON \n                | SEMICOLONtipo : INT \n            | FLOAT \n            | CHARfunction : FUNCTION tiporetorno ID LPAREN variables1 RPAREN SEMICOLON variables bloquebloque : LCBRACKET estatuto bloque1 \n            | LCBRACKET RCBRACKETbloque1 : RCBRACKET \n                | estatutoestatuto : asignacion \n                | retornofuncion \n                | lectura \n                | escritura\n                | decision\n                | repeticiontiporetorno : INT \n                | FLOATasignacion : ID EQUALS expresion SEMICOLON \n                | ID LBRACKET expresion RBRACKET EQUALS expresion SEMICOLONretornofuncion : RETURN LPAREN expresion RPAREN SEMICOLONexpresion : expresion PLUS expresion\n                | expresion MINUS expresion\n                | expresion TIMES expresion\n                | expresion DIVIDE expresion\n                | LPAREN expresion RPAREN\n                | INT\n                | FLOATlectura : READ LPAREN lectura1lectura1 : RPAREN SEMICOLON \n                | listaids lectura1escritura : WRITE LPAREN escritura1escritura1 : letrero escritura2 \n                | expresion escritura2escritura2 : RPAREN SEMICOLON \n                | escritura1letrero : QUOTES letrero1letrero1 : CHAR QUOTES \n                | CHAR letrero1repeticion : condicional\n                | nocondicionaldecision : IF LPAREN expresion RPAREN THEN bloque decision1decision1 : ELSE bloquecondicional : WHILE LPAREN expresion RPAREN DO bloquenocondicional : FOR ID EQUALS expresion TO expresion DO bloque'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,14,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[0,-1,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'ID':([2,15,16,17,18,19,20,21,22,23,24,25,26,27,33,34,36,40,41,42,46,52,53,54,55,63,65,66,76,84,85,86,88,89,96,104,105,112,113,116,119,120,124,125,],[3,28,37,-25,-26,39,28,-16,-19,-20,-21,-22,-23,-24,-48,-49,50,-18,-15,-17,39,-4,74,-6,-7,-37,39,-40,-27,-38,-39,-41,-44,-42,-5,-29,-43,-8,-7,-52,-28,-50,-51,-53,]),'SEMICOLON':([3,39,57,59,60,64,74,83,87,95,97,98,99,100,101,102,114,],[4,55,76,-35,-36,84,55,104,105,111,113,-30,-31,-32,-33,-34,119,]),'VARS':([4,111,],[6,6,]),'FUNCTION':([5,9,38,52,54,55,96,112,113,],[8,-2,-3,-4,-6,-7,-5,-8,-7,]),'INT':([6,8,43,44,45,47,48,49,51,56,58,59,60,67,68,72,77,78,79,80,90,98,99,100,101,102,103,106,107,110,],[11,17,59,59,59,59,59,59,11,75,59,-35,-36,59,59,59,59,59,59,59,-45,-30,-31,-32,-33,-34,59,-46,-47,59,]),'FLOAT':([6,8,43,44,45,47,48,49,51,58,59,60,67,68,72,77,78,79,80,90,98,99,100,101,102,103,106,107,110,],[12,18,60,60,60,60,60,60,12,60,-35,-36,60,60,60,60,60,60,60,-45,-30,-31,-32,-33,-34,60,-46,-47,60,]),'CHAR':([6,51,69,91,],[13,13,91,91,]),'LCBRACKET':([7,9,21,22,23,24,25,26,27,33,34,38,40,41,42,52,54,55,63,66,76,84,85,86,88,89,96,104,105,108,109,112,113,116,118,119,120,121,122,123,124,125,],[15,-2,-16,-19,-20,-21,-22,-23,-24,-48,-49,-3,-18,-15,-17,-4,-6,-7,-37,-40,-27,-38,-39,-41,-44,-42,-5,-29,-43,15,15,-8,-7,-52,15,-28,-50,15,15,-14,-51,-53,]),'COLON':([10,11,12,13,],[19,-11,-12,-13,]),'RCBRACKET':([15,20,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[21,42,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'RETURN':([15,20,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[29,29,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'READ':([15,20,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[30,30,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'WRITE':([15,20,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[31,31,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'IF':([15,20,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[32,32,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'WHILE':([15,20,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[35,35,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'FOR':([15,20,21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,116,119,120,124,125,],[36,36,-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,-52,-28,-50,-51,-53,]),'ELSE':([21,22,23,24,25,26,27,33,34,40,41,42,63,66,76,84,85,86,88,89,104,105,115,116,119,120,124,125,],[-16,-19,-20,-21,-22,-23,-24,-48,-49,-18,-15,-17,-37,-40,-27,-38,-39,-41,-44,-42,-29,-43,121,-52,-28,-50,-51,-53,]),'EQUALS':([28,50,82,],[43,72,103,]),'LBRACKET':([28,39,74,97,],[44,56,56,56,]),'LPAREN':([29,30,31,32,35,37,43,44,45,47,48,49,58,59,60,67,68,72,77,78,79,80,90,98,99,100,101,102,103,106,107,110,],[45,46,47,48,49,51,58,58,58,58,58,58,58,-35,-36,58,58,58,58,58,58,58,-45,-30,-31,-32,-33,-34,58,-46,-47,58,]),'RPAREN':([38,46,52,54,55,59,60,62,65,67,68,70,71,73,81,90,96,98,99,100,101,102,106,107,112,113,],[-3,64,-4,-6,-7,-35,-36,83,64,87,87,92,93,95,102,-45,-5,-30,-31,-32,-33,-34,-46,-47,-8,-7,]),'COMA':([39,74,97,],[53,53,53,]),'QUOTES':([47,59,60,67,68,90,91,98,99,100,101,102,106,107,],[69,-35,-36,69,69,-45,106,-30,-31,-32,-33,-34,-46,-47,]),'PLUS':([57,59,60,61,62,68,70,71,81,94,98,99,100,101,102,114,117,],[77,-35,-36,77,77,77,77,77,77,77,-30,-31,-32,-33,-34,77,77,]),'MINUS':([57,59,60,61,62,68,70,71,81,94,98,99,100,101,102,114,117,],[78,-35,-36,78,78,78,78,78,78,78,-30,-31,-32,-33,-34,78,78,]),'TIMES':([57,59,60,61,62,68,70,71,81,94,98,99,100,101,102,114,117,],[79,-35,-36,79,79,79,79,79,79,79,79,79,-32,-33,-34,79,79,]),'DIVIDE':([57,59,60,61,62,68,70,71,81,94,98,99,100,101,102,114,117,],[80,-35,-36,80,80,80,80,80,80,80,80,80,-32,-33,-34,80,80,]),'RBRACKET':([59,60,61,75,98,99,100,101,102,],[-35,-36,82,97,-30,-31,-32,-33,-34,]),'TO':([59,60,94,98,99,100,101,102,],[-35,-36,110,-30,-31,-32,-33,-34,]),'DO':([59,60,93,98,99,100,101,102,117,],[-35,-36,109,-30,-31,-32,-33,-34,122,]),'THEN':([92,],[108,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'variables':([4,111,],[5,118,]),'function':([5,],[7,]),'variables1':([6,51,],[9,73,]),'tipo':([6,51,],[10,10,]),'bloque':([7,108,109,118,121,122,],[14,115,116,123,124,125,]),'tiporetorno':([8,],[16,]),'estatuto':([15,20,],[20,40,]),'asignacion':([15,20,],[22,22,]),'retornofuncion':([15,20,],[23,23,]),'lectura':([15,20,],[24,24,]),'escritura':([15,20,],[25,25,]),'decision':([15,20,],[26,26,]),'repeticion':([15,20,],[27,27,]),'condicional':([15,20,],[33,33,]),'nocondicional':([15,20,],[34,34,]),'listaids':([19,46,65,],[38,65,65,]),'bloque1':([20,],[41,]),'listaids1':([39,74,97,],[52,96,112,]),'listaids2':([39,74,97,],[54,54,54,]),'expresion':([43,44,45,47,48,49,58,67,68,72,77,78,79,80,103,110,],[57,61,62,68,70,71,81,68,68,94,98,99,100,101,114,117,]),'lectura1':([46,65,],[63,85,]),'escritura1':([47,67,68,],[66,88,88,]),'letrero':([47,67,68,],[67,67,67,]),'escritura2':([67,68,],[86,89,]),'letrero1':([69,91,],[90,107,]),'decision1':([115,],[120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAMA ID SEMICOLON variables function bloque','programa',6,'p_programa','parser.py',10),
  ('variables -> VARS variables1','variables',2,'p_variables','parser.py',13),
  ('variables1 -> tipo COLON listaids','variables1',3,'p_variables1','parser.py',18),
  ('listaids -> ID listaids1','listaids',2,'p_listaids','parser.py',21),
  ('listaids1 -> COMA ID listaids1','listaids1',3,'p_listaids1','parser.py',24),
  ('listaids1 -> listaids2','listaids1',1,'p_listaids1','parser.py',25),
  ('listaids1 -> SEMICOLON','listaids1',1,'p_listaids1','parser.py',26),
  ('listaids2 -> LBRACKET INT RBRACKET listaids1','listaids2',4,'p_listaids2','parser.py',29),
  ('listaids2 -> LBRACKET INT RBRACKET SEMICOLON','listaids2',4,'p_listaids2','parser.py',30),
  ('listaids2 -> SEMICOLON','listaids2',1,'p_listaids2','parser.py',31),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',34),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',35),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',36),
  ('function -> FUNCTION tiporetorno ID LPAREN variables1 RPAREN SEMICOLON variables bloque','function',9,'p_function','parser.py',39),
  ('bloque -> LCBRACKET estatuto bloque1','bloque',3,'p_bloque','parser.py',42),
  ('bloque -> LCBRACKET RCBRACKET','bloque',2,'p_bloque','parser.py',43),
  ('bloque1 -> RCBRACKET','bloque1',1,'p_bloque1','parser.py',46),
  ('bloque1 -> estatuto','bloque1',1,'p_bloque1','parser.py',47),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',50),
  ('estatuto -> retornofuncion','estatuto',1,'p_estatuto','parser.py',51),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','parser.py',52),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','parser.py',53),
  ('estatuto -> decision','estatuto',1,'p_estatuto','parser.py',54),
  ('estatuto -> repeticion','estatuto',1,'p_estatuto','parser.py',55),
  ('tiporetorno -> INT','tiporetorno',1,'p_tiporetorno','parser.py',59),
  ('tiporetorno -> FLOAT','tiporetorno',1,'p_tiporetorno','parser.py',60),
  ('asignacion -> ID EQUALS expresion SEMICOLON','asignacion',4,'p_asignacion','parser.py',63),
  ('asignacion -> ID LBRACKET expresion RBRACKET EQUALS expresion SEMICOLON','asignacion',7,'p_asignacion','parser.py',64),
  ('retornofuncion -> RETURN LPAREN expresion RPAREN SEMICOLON','retornofuncion',5,'p_retornofuncion','parser.py',67),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion','parser.py',70),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion','parser.py',71),
  ('expresion -> expresion TIMES expresion','expresion',3,'p_expresion','parser.py',72),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion','parser.py',73),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_expresion','parser.py',74),
  ('expresion -> INT','expresion',1,'p_expresion','parser.py',75),
  ('expresion -> FLOAT','expresion',1,'p_expresion','parser.py',76),
  ('lectura -> READ LPAREN lectura1','lectura',3,'p_lectura','parser.py',79),
  ('lectura1 -> RPAREN SEMICOLON','lectura1',2,'p_lectura1','parser.py',82),
  ('lectura1 -> listaids lectura1','lectura1',2,'p_lectura1','parser.py',83),
  ('escritura -> WRITE LPAREN escritura1','escritura',3,'p_escritura','parser.py',86),
  ('escritura1 -> letrero escritura2','escritura1',2,'p_escritura1','parser.py',89),
  ('escritura1 -> expresion escritura2','escritura1',2,'p_escritura1','parser.py',90),
  ('escritura2 -> RPAREN SEMICOLON','escritura2',2,'p_escritura2','parser.py',93),
  ('escritura2 -> escritura1','escritura2',1,'p_escritura2','parser.py',94),
  ('letrero -> QUOTES letrero1','letrero',2,'p_letrero','parser.py',97),
  ('letrero1 -> CHAR QUOTES','letrero1',2,'p_letrero1','parser.py',100),
  ('letrero1 -> CHAR letrero1','letrero1',2,'p_letrero1','parser.py',101),
  ('repeticion -> condicional','repeticion',1,'p_repeticion','parser.py',104),
  ('repeticion -> nocondicional','repeticion',1,'p_repeticion','parser.py',105),
  ('decision -> IF LPAREN expresion RPAREN THEN bloque decision1','decision',7,'p_decision','parser.py',108),
  ('decision1 -> ELSE bloque','decision1',2,'p_decision1','parser.py',111),
  ('condicional -> WHILE LPAREN expresion RPAREN DO bloque','condicional',6,'p_condicional','parser.py',114),
  ('nocondicional -> FOR ID EQUALS expresion TO expresion DO bloque','nocondicional',8,'p_nocondicional','parser.py',117),
]
