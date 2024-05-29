lexer grammar PythonLexer;

LINE_BREAK: '\n';
TAB: '\t' | ' '' '' '' ';
SPACE: ' ';

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

DEF: 'def';
RETURN: 'return';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
STR_TYPE:'str';
BOOL_TYPE: 'bool';
DICT_TYPE: 'dict';
LIST_TYPE: 'list';
TUPLE_TYPE: 'tuple';
FUNCTION_TYPE: 'function';
OBJECT_TYPE: 'object';



BOOLEAN: 'True' | 'False';
NULL: 'None';
STRING: '"' PRINTABLE '"'
    | '\'' PRINTABLE '\''
    | '\'\'\'' (PRINTABLE | '\n')* '\'\'\''
    | '"""' (PRINTABLE | '\n')* '"""';

fragment AND: 'and' | '&';
fragment OR: 'or' | '|';
LOGICAL_OPERATOR: AND | OR;
NOT: 'not';

RELATIONS: '==' | '!=' | '<' | '>' | '<=' | '>=';

fragment ADD: '+';
fragment SUB: '-';
fragment MUL: '*';
fragment DIV: '/';
fragment MOD: '%';
fragment POW: '**';
fragment LSHIFT: '<<';
fragment RSHIFT: '>>';

ARITIMETIC_OPERATORS: ADD
   | SUB
   | MUL
   | DIV
   | MOD
   | POW
   ;

BIN_OPERATORS: LSHIFT
   | RSHIFT
   ;

fragment PRINTABLE: LETTERS_ | DIGIT | SPACE;

fragment LETTERS_: [a-zA-Z_];
fragment LETTERS: [a-zA-Z];
fragment DIGIT: [0-9];
fragment NON_ZERO_DIGIT: [1-9];

fragment INT: [+\-]? (NON_ZERO_DIGIT DIGIT* | '0'+);
fragment FLOAT: INT? '.' DIGIT*;
fragment REAL: INT | FLOAT;
fragment COMPLEX: [+\-]? REAL [jJ]
   | REAL [+\-] REAL [jJ];

NUMBER: REAL 
   | COMPLEX
   ;

WS: [\r\f]+ -> skip;

ID: LETTERS_ (LETTERS_ | DIGIT)?;