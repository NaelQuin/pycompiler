lexer grammar PythonLexer;

LINE_BREAK: '\n';
TAB: '\t';
SPACE: ' ';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
POW: '**';
LSHIFT: '<<';
RSHIFT: '>>';

ARITIMETIC_OPERATORS
   : ADD 
   | SUB 
   | MUL 
   | DIV 
   | MOD 
   | POW 
   | LSHIFT 
   | RSHIFT
   ;


WS
  : [ \r]+ -> skip
  ;