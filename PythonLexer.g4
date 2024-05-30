lexer grammar PythonLexer;

LINE_BREAK: '\n';
TAB: '\t' | ' '' '' '' ';
WS: ' ';

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

RANGE: 'range';
ENUMERATE: 'enumerate';
DEF: 'def';
RETURN: 'return';
IMPORT: 'import';
FROM: 'from';
AS: 'as';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
IN: 'in';
fragment INT_TYPE: 'int';
fragment FLOAT_TYPE: 'float';
fragment STR_TYPE:'str';
fragment BOOL_TYPE: 'bool';
fragment DICT_TYPE: 'dict';
fragment LIST_TYPE: 'list';
fragment TUPLE_TYPE: 'tuple';
fragment FUNCTION_TYPE: 'function';
fragment OBJECT_TYPE: 'object';
SET_TYPE: 'set';

TYPE: INT_TYPE | FLOAT_TYPE | STR_TYPE | BOOL_TYPE | DICT_TYPE | LIST_TYPE | TUPLE_TYPE | FUNCTION_TYPE | OBJECT_TYPE;

BOOLEAN: 'True' | 'False';
NULL: 'None';
STRING: '"' PRINTABLE '"'
    | '\'' PRINTABLE '\''
    | '\'\'\'' (PRINTABLE | '\n')* '\'\'\''
    | '"""' (PRINTABLE | '\n')* '"""'
    ;

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

ID: LETTERS_ (LETTERS_ | DIGIT)*;

fragment PRINTABLE: LETTERS_ | DIGIT | WS;

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

WS_: [\r\f]+ -> skip;