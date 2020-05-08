
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE ELSEIF EQORGT EQORLESS EQUAL EYE FLOATNUM FOR ID IF INTNUM MULASSIGN NOTEQUAL ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROS\n    CODE : INSTRUCTIONS\n    \n    INSTRUCTIONS : \'{\' INSTRUCTIONS \'}\'\n                | INSTRUCTION INSTRUCTIONS\n                | INSTRUCTION\n    \n    INSTRUCTION : ASSIGN \';\'\n                | IF_CONDITION\n                | FOR_LOOP\n                | WHILE_LOOP\n                | CONTROL_INSTRUCTION \';\'\n                | PRINT_CALL \';\'\n    \n    ASSIGN : ID ASSIGN_TYPE EXPRESSION\n           | ID \'[\' INTNUM \']\' ASSIGN_TYPE EXPRESSION\n           | ID \'[\' INTNUM \',\' INTNUM \']\' ASSIGN_TYPE EXPRESSION\n    \n    ASSIGN_TYPE : \'=\'\n                | ADDASSIGN\n                | SUBASSIGN\n                | DIVASSIGN\n                | MULASSIGN\n    \n    EXPRESSION : BINARY_EXPRESSION\n               | LOGICAL_EXPRESSION\n               | MATRIX_EXPRESSION\n               | \'(\' EXPRESSION \')\'\n               | TERM\n    \n    BINARY_EXPRESSION : EXPRESSION \'+\' EXPRESSION\n                      | EXPRESSION \'-\' EXPRESSION\n                      | EXPRESSION \'*\' EXPRESSION\n                      | EXPRESSION \'/\' EXPRESSION\n    \n    LOGICAL_EXPRESSION : EXPRESSION \'>\' EXPRESSION\n                      | EXPRESSION \'<\' EXPRESSION\n                      | EXPRESSION EQORGT EXPRESSION\n                      | EXPRESSION EQORLESS EXPRESSION\n                      | EXPRESSION EQUAL EXPRESSION\n                      | EXPRESSION NOTEQUAL EXPRESSION\n    \n    MATRIX_EXPRESSION : EXPRESSION DOTADD EXPRESSION\n                      | EXPRESSION DOTSUB EXPRESSION\n                      | EXPRESSION DOTMUL EXPRESSION\n                      | EXPRESSION DOTDIV EXPRESSION\n    \n    TERM : ID\n         | INTNUM\n         | FLOATNUM\n         | STRING\n         | MATRIX\n         | FUNCTION_CALL\n         | ID "\'"\n         | \'-\' ID\n    \n    EXPRESSION : RETURN TERM\n    \n    INTNUM_OR_ID : INTNUM\n                 | ID\n    \n    MATRIX : \'[\' VECTORS \']\'\n    \n    VECTORS : VECTORS \';\' VECTOR\n            | VECTOR\n    \n    VECTOR : VECTOR \',\' TERM\n           | TERM\n    \n    FUNCTION_CALL : FUNCTION_NAME \'(\' TERM \')\'\n    \n    FUNCTION_NAME : ZEROS\n                  | ONES\n                  | EYE\n    \n    CONTROL_INSTRUCTION : BREAK\n                        | CONTINUE\n                        | RETURN\n                        | RETURN TERM\n    \n    PRINT_CALL : PRINT PRINT_TERMS\n    \n    PRINT_TERMS : PRINT_TERMS \',\' TERM\n                | TERM\n    \n    IF_CONDITION    : IF \'(\' LOGICAL_EXPRESSION \')\' INSTRUCTION ELIF_STATEMENTS ELSE_STATEMENT\n                    | IF \'(\' LOGICAL_EXPRESSION \')\' \'{\' INSTRUCTIONS \'}\' ELIF_STATEMENTS ELSE_STATEMENT\n    ELIF_STATEMENTS : ELSEIF \'(\' LOGICAL_EXPRESSION \')\' INSTRUCTION ELIF_STATEMENTS\n                    | ELSEIF \'(\' LOGICAL_EXPRESSION \')\' \'{\' INSTRUCTIONS \'}\' ELIF_STATEMENTS\n                    | ELSEIF \'(\' LOGICAL_EXPRESSION \')\' INSTRUCTION\n                    | ELSEIF \'(\' LOGICAL_EXPRESSION \')\' \'{\' INSTRUCTIONS \'}\'\n    ELSE_STATEMENT  : ELSE INSTRUCTION\n                    | ELSE \'{\' INSTRUCTIONS \'}\'\n                    |\n    \n    FOR_LOOP : FOR FOR_CONDITION \'{\' INSTRUCTIONS \'}\'\n             | FOR FOR_CONDITION  INSTRUCTION\n    \n    FOR_CONDITION : TERM \'=\' INTNUM_OR_ID \':\' INTNUM_OR_ID\n    \n    WHILE_LOOP : WHILE \'(\' LOGICAL_EXPRESSION \')\' \'{\' INSTRUCTIONS \'}\'\n               | WHILE \'(\' LOGICAL_EXPRESSION \')\' INSTRUCTION\n    '
    
_lr_action_items = {'{':([0,3,4,6,7,8,21,22,23,32,61,62,90,93,94,99,119,120,125,126,129,132,135,136,139,141,142,144,146,147,148,149,150,151,153,154,],[3,3,3,-6,-7,-8,-5,-9,-10,61,3,-75,119,-47,-48,125,3,-74,3,-78,-73,-76,-65,142,-77,-71,3,-73,150,-66,-72,-69,3,-67,-70,-68,]),'ID':([0,3,4,6,7,8,13,17,18,21,22,23,24,26,27,28,29,30,31,32,40,41,46,55,57,61,62,63,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,90,93,94,96,97,99,116,119,120,121,125,126,129,132,134,135,136,137,139,141,142,144,146,147,148,149,150,151,153,154,],[11,11,11,-6,-7,-8,34,34,34,-5,-9,-10,34,-14,-15,-16,-17,-18,34,11,65,34,34,34,34,11,-75,94,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,11,-47,-48,34,34,11,34,11,-74,94,11,-78,-73,-76,34,-65,11,34,-77,-71,11,-73,11,-66,-72,-69,11,-67,-70,-68,]),'IF':([0,3,4,6,7,8,21,22,23,32,61,62,90,93,94,99,119,120,125,126,129,132,135,136,139,141,142,144,146,147,148,149,150,151,153,154,],[12,12,12,-6,-7,-8,-5,-9,-10,12,12,-75,12,-47,-48,12,12,-74,12,-78,-73,-76,-65,12,-77,-71,12,-73,12,-66,-72,-69,12,-67,-70,-68,]),'FOR':([0,3,4,6,7,8,21,22,23,32,61,62,90,93,94,99,119,120,125,126,129,132,135,136,139,141,142,144,146,147,148,149,150,151,153,154,],[13,13,13,-6,-7,-8,-5,-9,-10,13,13,-75,13,-47,-48,13,13,-74,13,-78,-73,-76,-65,13,-77,-71,13,-73,13,-66,-72,-69,13,-67,-70,-68,]),'WHILE':([0,3,4,6,7,8,21,22,23,32,61,62,90,93,94,99,119,120,125,126,129,132,135,136,139,141,142,144,146,147,148,149,150,151,153,154,],[14,14,14,-6,-7,-8,-5,-9,-10,14,14,-75,14,-47,-48,14,14,-74,14,-78,-73,-76,-65,14,-77,-71,14,-73,14,-66,-72,-69,14,-67,-70,-68,]),'BREAK':([0,3,4,6,7,8,21,22,23,32,61,62,90,93,94,99,119,120,125,126,129,132,135,136,139,141,142,144,146,147,148,149,150,151,153,154,],[15,15,15,-6,-7,-8,-5,-9,-10,15,15,-75,15,-47,-48,15,15,-74,15,-78,-73,-76,-65,15,-77,-71,15,-73,15,-66,-72,-69,15,-67,-70,-68,]),'CONTINUE':([0,3,4,6,7,8,21,22,23,32,61,62,90,93,94,99,119,120,125,126,129,132,135,136,139,141,142,144,146,147,148,149,150,151,153,154,],[16,16,16,-6,-7,-8,-5,-9,-10,16,16,-75,16,-47,-48,16,16,-74,16,-78,-73,-76,-65,16,-77,-71,16,-73,16,-66,-72,-69,16,-67,-70,-68,]),'RETURN':([0,3,4,6,7,8,21,22,23,24,26,27,28,29,30,31,32,46,55,61,62,72,73,74,75,76,77,78,79,80,81,82,83,84,85,90,93,94,99,116,119,120,125,126,129,132,134,135,136,137,139,141,142,144,146,147,148,149,150,151,153,154,],[17,17,17,-6,-7,-8,-5,-9,-10,57,-14,-15,-16,-17,-18,57,17,57,57,17,-75,57,57,57,57,57,57,57,57,57,57,57,57,57,57,17,-47,-48,17,57,17,-74,17,-78,-73,-76,57,-65,17,57,-77,-71,17,-73,17,-66,-72,-69,17,-67,-70,-68,]),'PRINT':([0,3,4,6,7,8,21,22,23,32,61,62,90,93,94,99,119,120,125,126,129,132,135,136,139,141,142,144,146,147,148,149,150,151,153,154,],[18,18,18,-6,-7,-8,-5,-9,-10,18,18,-75,18,-47,-48,18,18,-74,18,-78,-73,-76,-65,18,-77,-71,18,-73,18,-66,-72,-69,18,-67,-70,-68,]),'$end':([1,2,4,6,7,8,20,21,22,23,50,62,120,126,129,135,139,141,144,147,148,149,151,153,154,],[0,-1,-4,-6,-7,-8,-3,-5,-9,-10,-2,-75,-74,-78,-73,-65,-77,-71,-73,-66,-72,-69,-67,-70,-68,]),'}':([4,6,7,8,19,20,21,22,23,50,62,91,120,126,129,131,133,135,139,141,144,145,147,148,149,151,152,153,154,],[-4,-6,-7,-8,50,-3,-5,-9,-10,-2,-75,120,-74,-78,-73,138,139,-65,-77,-71,-73,148,-66,-72,-69,-67,153,-70,-68,]),';':([5,9,10,15,16,17,34,35,36,37,38,39,47,48,49,51,52,53,54,56,64,65,66,67,68,87,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,122,123,124,127,140,],[21,22,23,-58,-59,-60,-38,-39,-40,-41,-42,-43,-61,-62,-64,-11,-19,-20,-21,-23,-44,-45,96,-51,-53,-46,-49,-63,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-22,-50,-52,-54,-12,-13,]),'ELSEIF':([6,7,8,21,22,23,62,118,120,126,129,135,138,139,141,144,147,148,149,151,153,154,],[-6,-7,-8,-5,-9,-10,-75,130,-74,-78,-73,-65,130,-77,-71,-73,-66,-72,130,-67,130,-68,]),'ELSE':([6,7,8,21,22,23,62,120,126,129,135,139,141,144,147,148,149,151,153,154,],[-6,-7,-8,-5,-9,-10,-75,-74,-78,136,-65,-77,-71,136,-66,-72,-69,-67,-70,-68,]),'[':([11,13,17,18,24,26,27,28,29,30,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[25,41,41,41,41,-14,-15,-16,-17,-18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'=':([11,33,34,35,36,37,38,39,64,65,88,95,124,128,],[26,63,-38,-39,-40,-41,-42,-43,-44,-45,26,-49,-54,26,]),'ADDASSIGN':([11,88,128,],[27,27,27,]),'SUBASSIGN':([11,88,128,],[28,28,28,]),'DIVASSIGN':([11,88,128,],[29,29,29,]),'MULASSIGN':([11,88,128,],[30,30,30,]),'(':([12,14,24,26,27,28,29,30,31,42,43,44,45,46,55,72,73,74,75,76,77,78,79,80,81,82,83,84,85,116,130,134,137,],[31,46,55,-14,-15,-16,-17,-18,55,69,-55,-56,-57,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,137,55,55,]),'INTNUM':([13,17,18,24,25,26,27,28,29,30,31,41,46,55,57,63,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,89,96,97,116,121,134,137,],[35,35,35,35,58,-14,-15,-16,-17,-18,35,35,35,35,35,93,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,117,35,35,35,93,35,35,]),'FLOATNUM':([13,17,18,24,26,27,28,29,30,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[36,36,36,36,-14,-15,-16,-17,-18,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'STRING':([13,17,18,24,26,27,28,29,30,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[37,37,37,37,-14,-15,-16,-17,-18,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'-':([13,17,18,24,26,27,28,29,30,31,34,35,36,37,38,39,41,46,51,52,53,54,55,56,57,59,60,64,65,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,95,96,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,124,127,134,137,140,143,],[40,40,40,40,-14,-15,-16,-17,-18,40,-38,-39,-40,-41,-42,-43,40,40,73,-19,-20,-21,40,-23,40,-20,73,-44,-45,40,-20,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,73,-46,-49,40,40,73,73,73,73,73,73,73,73,73,73,73,73,73,73,-22,40,-54,73,40,40,73,-20,]),'ZEROS':([13,17,18,24,26,27,28,29,30,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[43,43,43,43,-14,-15,-16,-17,-18,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'ONES':([13,17,18,24,26,27,28,29,30,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[44,44,44,44,-14,-15,-16,-17,-18,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'EYE':([13,17,18,24,26,27,28,29,30,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[45,45,45,45,-14,-15,-16,-17,-18,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),',':([34,35,36,37,38,39,48,49,58,64,65,67,68,95,100,122,123,124,],[-38,-39,-40,-41,-42,-43,71,-64,89,-44,-45,97,-53,-49,-63,97,-52,-54,]),'+':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,72,-19,-20,-21,-23,-20,72,-44,-45,-20,72,-46,-49,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-22,-54,72,72,-20,]),'*':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,74,-19,-20,-21,-23,-20,74,-44,-45,-20,74,-46,-49,74,74,74,74,74,74,74,74,74,74,74,74,74,74,-22,-54,74,74,-20,]),'/':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,75,-19,-20,-21,-23,-20,75,-44,-45,-20,75,-46,-49,75,75,75,75,75,75,75,75,75,75,75,75,75,75,-22,-54,75,75,-20,]),'>':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,76,-19,-20,-21,-23,-20,76,-44,-45,-20,76,-46,-49,76,76,76,76,76,76,76,76,76,76,76,76,76,76,-22,-54,76,76,-20,]),'<':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,77,-19,-20,-21,-23,-20,77,-44,-45,-20,77,-46,-49,77,77,77,77,77,77,77,77,77,77,77,77,77,77,-22,-54,77,77,-20,]),'EQORGT':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,78,-19,-20,-21,-23,-20,78,-44,-45,-20,78,-46,-49,78,78,78,78,78,78,78,78,78,78,78,78,78,78,-22,-54,78,78,-20,]),'EQORLESS':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,79,-19,-20,-21,-23,-20,79,-44,-45,-20,79,-46,-49,79,79,79,79,79,79,79,79,79,79,79,79,79,79,-22,-54,79,79,-20,]),'EQUAL':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,80,-19,-20,-21,-23,-20,80,-44,-45,-20,80,-46,-49,80,80,80,80,80,80,80,80,80,80,80,80,80,80,-22,-54,80,80,-20,]),'NOTEQUAL':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,81,-19,-20,-21,-23,-20,81,-44,-45,-20,81,-46,-49,81,81,81,81,81,81,81,81,81,81,81,81,81,81,-22,-54,81,81,-20,]),'DOTADD':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,82,-19,-20,-21,-23,-20,82,-44,-45,-20,82,-46,-49,82,82,82,82,82,82,82,82,82,82,82,82,82,82,-22,-54,82,82,-20,]),'DOTSUB':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,83,-19,-20,-21,-23,-20,83,-44,-45,-20,83,-46,-49,83,83,83,83,83,83,83,83,83,83,83,83,83,83,-22,-54,83,83,-20,]),'DOTMUL':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,84,-19,-20,-21,-23,-20,84,-44,-45,-20,84,-46,-49,84,84,84,84,84,84,84,84,84,84,84,84,84,84,-22,-54,84,84,-20,]),'DOTDIV':([34,35,36,37,38,39,51,52,53,54,56,59,60,64,65,70,86,87,95,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,127,140,143,],[-38,-39,-40,-41,-42,-43,85,-19,-20,-21,-23,-20,85,-44,-45,-20,85,-46,-49,85,85,85,85,85,85,85,85,85,85,85,85,85,85,-22,-54,85,85,-20,]),']':([34,35,36,37,38,39,58,64,65,66,67,68,95,117,122,123,124,],[-38,-39,-40,-41,-42,-43,88,-44,-45,95,-51,-53,-49,128,-50,-52,-54,]),')':([34,35,36,37,38,39,52,53,54,56,59,64,65,70,86,87,95,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,124,143,],[-38,-39,-40,-41,-42,-43,-19,-20,-21,-23,90,-44,-45,99,115,-46,-49,124,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-22,-54,146,]),"'":([34,],[64,]),':':([92,93,94,],[121,-47,-48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'CODE':([0,],[1,]),'INSTRUCTIONS':([0,3,4,61,119,125,142,150,],[2,19,20,91,131,133,145,152,]),'INSTRUCTION':([0,3,4,32,61,90,99,119,125,136,142,146,150,],[4,4,4,62,4,118,126,4,4,141,4,149,4,]),'ASSIGN':([0,3,4,32,61,90,99,119,125,136,142,146,150,],[5,5,5,5,5,5,5,5,5,5,5,5,5,]),'IF_CONDITION':([0,3,4,32,61,90,99,119,125,136,142,146,150,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'FOR_LOOP':([0,3,4,32,61,90,99,119,125,136,142,146,150,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'WHILE_LOOP':([0,3,4,32,61,90,99,119,125,136,142,146,150,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'CONTROL_INSTRUCTION':([0,3,4,32,61,90,99,119,125,136,142,146,150,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'PRINT_CALL':([0,3,4,32,61,90,99,119,125,136,142,146,150,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ASSIGN_TYPE':([11,88,128,],[24,116,134,]),'FOR_CONDITION':([13,],[32,]),'TERM':([13,17,18,24,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[33,47,49,56,56,68,56,56,87,98,100,56,56,56,56,56,56,56,56,56,56,56,56,56,56,68,123,56,56,56,]),'MATRIX':([13,17,18,24,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FUNCTION_CALL':([13,17,18,24,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'FUNCTION_NAME':([13,17,18,24,31,41,46,55,57,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,96,97,116,134,137,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'PRINT_TERMS':([18,],[48,]),'EXPRESSION':([24,31,46,55,72,73,74,75,76,77,78,79,80,81,82,83,84,85,116,134,137,],[51,60,60,86,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,140,60,]),'BINARY_EXPRESSION':([24,31,46,55,72,73,74,75,76,77,78,79,80,81,82,83,84,85,116,134,137,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'LOGICAL_EXPRESSION':([24,31,46,55,72,73,74,75,76,77,78,79,80,81,82,83,84,85,116,134,137,],[53,59,70,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,143,]),'MATRIX_EXPRESSION':([24,31,46,55,72,73,74,75,76,77,78,79,80,81,82,83,84,85,116,134,137,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'VECTORS':([41,],[66,]),'VECTOR':([41,96,],[67,122,]),'INTNUM_OR_ID':([63,121,],[92,132,]),'ELIF_STATEMENTS':([118,138,149,153,],[129,144,151,154,]),'ELSE_STATEMENT':([129,144,],[135,147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> CODE","S'",1,None,None,None),
  ('CODE -> INSTRUCTIONS','CODE',1,'p_code','custom_parser.py',39),
  ('INSTRUCTIONS -> { INSTRUCTIONS }','INSTRUCTIONS',3,'p_instructions','custom_parser.py',46),
  ('INSTRUCTIONS -> INSTRUCTION INSTRUCTIONS','INSTRUCTIONS',2,'p_instructions','custom_parser.py',47),
  ('INSTRUCTIONS -> INSTRUCTION','INSTRUCTIONS',1,'p_instructions','custom_parser.py',48),
  ('INSTRUCTION -> ASSIGN ;','INSTRUCTION',2,'p_instruction','custom_parser.py',60),
  ('INSTRUCTION -> IF_CONDITION','INSTRUCTION',1,'p_instruction','custom_parser.py',61),
  ('INSTRUCTION -> FOR_LOOP','INSTRUCTION',1,'p_instruction','custom_parser.py',62),
  ('INSTRUCTION -> WHILE_LOOP','INSTRUCTION',1,'p_instruction','custom_parser.py',63),
  ('INSTRUCTION -> CONTROL_INSTRUCTION ;','INSTRUCTION',2,'p_instruction','custom_parser.py',64),
  ('INSTRUCTION -> PRINT_CALL ;','INSTRUCTION',2,'p_instruction','custom_parser.py',65),
  ('ASSIGN -> ID ASSIGN_TYPE EXPRESSION','ASSIGN',3,'p_assign','custom_parser.py',72),
  ('ASSIGN -> ID [ INTNUM ] ASSIGN_TYPE EXPRESSION','ASSIGN',6,'p_assign','custom_parser.py',73),
  ('ASSIGN -> ID [ INTNUM , INTNUM ] ASSIGN_TYPE EXPRESSION','ASSIGN',8,'p_assign','custom_parser.py',74),
  ('ASSIGN_TYPE -> =','ASSIGN_TYPE',1,'p_assign_type','custom_parser.py',86),
  ('ASSIGN_TYPE -> ADDASSIGN','ASSIGN_TYPE',1,'p_assign_type','custom_parser.py',87),
  ('ASSIGN_TYPE -> SUBASSIGN','ASSIGN_TYPE',1,'p_assign_type','custom_parser.py',88),
  ('ASSIGN_TYPE -> DIVASSIGN','ASSIGN_TYPE',1,'p_assign_type','custom_parser.py',89),
  ('ASSIGN_TYPE -> MULASSIGN','ASSIGN_TYPE',1,'p_assign_type','custom_parser.py',90),
  ('EXPRESSION -> BINARY_EXPRESSION','EXPRESSION',1,'p_expression','custom_parser.py',97),
  ('EXPRESSION -> LOGICAL_EXPRESSION','EXPRESSION',1,'p_expression','custom_parser.py',98),
  ('EXPRESSION -> MATRIX_EXPRESSION','EXPRESSION',1,'p_expression','custom_parser.py',99),
  ('EXPRESSION -> ( EXPRESSION )','EXPRESSION',3,'p_expression','custom_parser.py',100),
  ('EXPRESSION -> TERM','EXPRESSION',1,'p_expression','custom_parser.py',101),
  ('BINARY_EXPRESSION -> EXPRESSION + EXPRESSION','BINARY_EXPRESSION',3,'p_binary_expression','custom_parser.py',111),
  ('BINARY_EXPRESSION -> EXPRESSION - EXPRESSION','BINARY_EXPRESSION',3,'p_binary_expression','custom_parser.py',112),
  ('BINARY_EXPRESSION -> EXPRESSION * EXPRESSION','BINARY_EXPRESSION',3,'p_binary_expression','custom_parser.py',113),
  ('BINARY_EXPRESSION -> EXPRESSION / EXPRESSION','BINARY_EXPRESSION',3,'p_binary_expression','custom_parser.py',114),
  ('LOGICAL_EXPRESSION -> EXPRESSION > EXPRESSION','LOGICAL_EXPRESSION',3,'p_logical_expression','custom_parser.py',121),
  ('LOGICAL_EXPRESSION -> EXPRESSION < EXPRESSION','LOGICAL_EXPRESSION',3,'p_logical_expression','custom_parser.py',122),
  ('LOGICAL_EXPRESSION -> EXPRESSION EQORGT EXPRESSION','LOGICAL_EXPRESSION',3,'p_logical_expression','custom_parser.py',123),
  ('LOGICAL_EXPRESSION -> EXPRESSION EQORLESS EXPRESSION','LOGICAL_EXPRESSION',3,'p_logical_expression','custom_parser.py',124),
  ('LOGICAL_EXPRESSION -> EXPRESSION EQUAL EXPRESSION','LOGICAL_EXPRESSION',3,'p_logical_expression','custom_parser.py',125),
  ('LOGICAL_EXPRESSION -> EXPRESSION NOTEQUAL EXPRESSION','LOGICAL_EXPRESSION',3,'p_logical_expression','custom_parser.py',126),
  ('MATRIX_EXPRESSION -> EXPRESSION DOTADD EXPRESSION','MATRIX_EXPRESSION',3,'p_matrix_expression','custom_parser.py',133),
  ('MATRIX_EXPRESSION -> EXPRESSION DOTSUB EXPRESSION','MATRIX_EXPRESSION',3,'p_matrix_expression','custom_parser.py',134),
  ('MATRIX_EXPRESSION -> EXPRESSION DOTMUL EXPRESSION','MATRIX_EXPRESSION',3,'p_matrix_expression','custom_parser.py',135),
  ('MATRIX_EXPRESSION -> EXPRESSION DOTDIV EXPRESSION','MATRIX_EXPRESSION',3,'p_matrix_expression','custom_parser.py',136),
  ('TERM -> ID','TERM',1,'p_term','custom_parser.py',143),
  ('TERM -> INTNUM','TERM',1,'p_term','custom_parser.py',144),
  ('TERM -> FLOATNUM','TERM',1,'p_term','custom_parser.py',145),
  ('TERM -> STRING','TERM',1,'p_term','custom_parser.py',146),
  ('TERM -> MATRIX','TERM',1,'p_term','custom_parser.py',147),
  ('TERM -> FUNCTION_CALL','TERM',1,'p_term','custom_parser.py',148),
  ("TERM -> ID '",'TERM',2,'p_term','custom_parser.py',149),
  ('TERM -> - ID','TERM',2,'p_term','custom_parser.py',150),
  ('EXPRESSION -> RETURN TERM','EXPRESSION',2,'p_return','custom_parser.py',167),
  ('INTNUM_OR_ID -> INTNUM','INTNUM_OR_ID',1,'p_intnum_or_id','custom_parser.py',174),
  ('INTNUM_OR_ID -> ID','INTNUM_OR_ID',1,'p_intnum_or_id','custom_parser.py',175),
  ('MATRIX -> [ VECTORS ]','MATRIX',3,'p_matrix','custom_parser.py',186),
  ('VECTORS -> VECTORS ; VECTOR','VECTORS',3,'p_vectors','custom_parser.py',193),
  ('VECTORS -> VECTOR','VECTORS',1,'p_vectors','custom_parser.py',194),
  ('VECTOR -> VECTOR , TERM','VECTOR',3,'p_vector','custom_parser.py',204),
  ('VECTOR -> TERM','VECTOR',1,'p_vector','custom_parser.py',205),
  ('FUNCTION_CALL -> FUNCTION_NAME ( TERM )','FUNCTION_CALL',4,'p_function_call','custom_parser.py',216),
  ('FUNCTION_NAME -> ZEROS','FUNCTION_NAME',1,'p_function_name','custom_parser.py',223),
  ('FUNCTION_NAME -> ONES','FUNCTION_NAME',1,'p_function_name','custom_parser.py',224),
  ('FUNCTION_NAME -> EYE','FUNCTION_NAME',1,'p_function_name','custom_parser.py',225),
  ('CONTROL_INSTRUCTION -> BREAK','CONTROL_INSTRUCTION',1,'p_control_instruction','custom_parser.py',232),
  ('CONTROL_INSTRUCTION -> CONTINUE','CONTROL_INSTRUCTION',1,'p_control_instruction','custom_parser.py',233),
  ('CONTROL_INSTRUCTION -> RETURN','CONTROL_INSTRUCTION',1,'p_control_instruction','custom_parser.py',234),
  ('CONTROL_INSTRUCTION -> RETURN TERM','CONTROL_INSTRUCTION',2,'p_control_instruction','custom_parser.py',235),
  ('PRINT_CALL -> PRINT PRINT_TERMS','PRINT_CALL',2,'p_print_call','custom_parser.py',245),
  ('PRINT_TERMS -> PRINT_TERMS , TERM','PRINT_TERMS',3,'p_print_terms','custom_parser.py',252),
  ('PRINT_TERMS -> TERM','PRINT_TERMS',1,'p_print_terms','custom_parser.py',253),
  ('IF_CONDITION -> IF ( LOGICAL_EXPRESSION ) INSTRUCTION ELIF_STATEMENTS ELSE_STATEMENT','IF_CONDITION',7,'p_if_condition','custom_parser.py',263),
  ('IF_CONDITION -> IF ( LOGICAL_EXPRESSION ) { INSTRUCTIONS } ELIF_STATEMENTS ELSE_STATEMENT','IF_CONDITION',9,'p_if_condition','custom_parser.py',264),
  ('ELIF_STATEMENTS -> ELSEIF ( LOGICAL_EXPRESSION ) INSTRUCTION ELIF_STATEMENTS','ELIF_STATEMENTS',6,'p_if_condition','custom_parser.py',265),
  ('ELIF_STATEMENTS -> ELSEIF ( LOGICAL_EXPRESSION ) { INSTRUCTIONS } ELIF_STATEMENTS','ELIF_STATEMENTS',8,'p_if_condition','custom_parser.py',266),
  ('ELIF_STATEMENTS -> ELSEIF ( LOGICAL_EXPRESSION ) INSTRUCTION','ELIF_STATEMENTS',5,'p_if_condition','custom_parser.py',267),
  ('ELIF_STATEMENTS -> ELSEIF ( LOGICAL_EXPRESSION ) { INSTRUCTIONS }','ELIF_STATEMENTS',7,'p_if_condition','custom_parser.py',268),
  ('ELSE_STATEMENT -> ELSE INSTRUCTION','ELSE_STATEMENT',2,'p_if_condition','custom_parser.py',269),
  ('ELSE_STATEMENT -> ELSE { INSTRUCTIONS }','ELSE_STATEMENT',4,'p_if_condition','custom_parser.py',270),
  ('ELSE_STATEMENT -> <empty>','ELSE_STATEMENT',0,'p_if_condition','custom_parser.py',271),
  ('FOR_LOOP -> FOR FOR_CONDITION { INSTRUCTIONS }','FOR_LOOP',5,'p_for_loop','custom_parser.py',296),
  ('FOR_LOOP -> FOR FOR_CONDITION INSTRUCTION','FOR_LOOP',3,'p_for_loop','custom_parser.py',297),
  ('FOR_CONDITION -> TERM = INTNUM_OR_ID : INTNUM_OR_ID','FOR_CONDITION',5,'p_for_condition','custom_parser.py',307),
  ('WHILE_LOOP -> WHILE ( LOGICAL_EXPRESSION ) { INSTRUCTIONS }','WHILE_LOOP',7,'p_while_loop','custom_parser.py',314),
  ('WHILE_LOOP -> WHILE ( LOGICAL_EXPRESSION ) INSTRUCTION','WHILE_LOOP',5,'p_while_loop','custom_parser.py',315),
]
