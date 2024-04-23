lexer grammar PythonLexer;

LINE_BREAK: '\n';
BEGIN_LINE: '\r';
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

LAMBDA: 'lambda';
NOT: 'not';
fragment LT: '<';
fragment GT: '>';
fragment EQ: '==';
fragment NEQ: '!=';
fragment LEQ: '<=';
fragment GEQ: '>=';
RELATIONS
   : LT
   | GT
   | EQ
   | NEQ
   | LEQ
   | GEQ
   ;
LPARENTHESIS: '(';
RPARENTHESIS: ')';
LBRACKET: '[';
RBRACKET: ']';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
ASSIGN: '=';
DOT: '.';
COLON: ':';
SEMI: ';';
HASH: '#';

LOGICAL_OPERATOR
   : 'and' | 'or' | '&' | '|'
   ;

NULL
   : 'None'
   ;

BOOLEAN
   : 'True' | 'False'
   ;

ID
   : [a-zA-Z_] [a-zA-Z_0-9]*
   ;

INDENT
   : '  '
   | TAB
   ;

fragment SYMBOLS
   : '!' | '@' | '#' | '$' | '%' | '^' | '&' | '*' | '(' | ')' | '-' | '+' | '=' | '|' | '~' | ',' | '.' | ':' | ';' | '<' | '>' | '?' | '[' | ']' | '{' | '}' | '/' | '\\' | '\'' | '"' | '_'
   ;

STRING
   : '"' (ESC | ~ ["\\])* '"'
   | '\'' (ESC | ~ ["\\])* '\''
   | '"""' (ESC | ~ ["\\])* '"""'
   | '\'\'\'' (ESC | ~ ["\\])* '\'\'\''
   ;
fragment ESC
   : '\\' (["'\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;

NUMBER
   : INT 
   | DOUBLE  
   | COMPLEX 
   | HEXADECIMAL
   | OCTAL
   ;

fragment INT
  : [0-9]+ //| [1-9] [0-9]*
  ;

fragment DOUBLE
   : INT '.' [0-9]* EXP?
   ;

fragment COMPLEX
   :  DOUBLE? [+\-]? DOUBLE 'j'
   ;

fragment HEXADECIMAL
   : '0x' HEX*
   ;

fragment OCTAL
   : '0o' [0-7]*
   ;


// EXP we use "\-" since "-" means "range" inside [...]
EXP
   : [Ee] [+\-]? INT
   ;

WS
  : [ \r]+ -> skip
  ;