parser grammar PythonParser;

options {
  tokenVocab = PythonLexer;
}

code: (importing | stat | '\n')* EOF;

importing: 'import' WS+ ID ('.' ID)* asStat?
  | 'from' WS+ ID ('.' ID)* WS+ 'import' WS+ ID (WS* ',' WS* ID)* asStat?
  ;

asStat: WS+ 'as' WS+ ID;

statIndent: TAB stat;

stat: statPossibility '\n'?;

statPossibility: func
  | expr
  | query
  | assignment
  | conditional
  | forLoop
  | whileLoop
  ;

whileLoop: 'while' condition ':' '\n'
  statIndent* '\n';

forLoop: 'for' varLoop 'in' WS+ (loopList | ID) ':' '\n'
  statIndent* '\n';

varLoop: WS+ ID WS+ (',' WS* ID)*;
loopList: iterable | range | enumerate;

iterable: list | tuple | STRING | set | dict;
range: 'range' '(' expr? (',' expr)? (',' expr)? ')';
enumerate: 'enumerate' '(' (iterable | ID) ')';

conditional: 'if' condition ':' '\n' statIndent*
  ('elif' condition ':' '\n' statIndent*)*
  ('else' ':' '\n' statIndent*)?
  ;

condition: WS query;

func: 'def' WS+ ID '(' params? ')' WS* ':' '\n' statIndent*
  TAB+ 'return' WS+ expr? '\n';

params: paramCase (',' paramCase)*;

paramCase: ID varType? paramDefault?;
paramDefault: WS* '=' WS* expr WS*;

varType: WS* ':' WS* TYPE;

assignment: ID varType? WS* '=' WS* (expr | query);

query: BOOLEAN                   # boolean
  | ID                           # queryId
  | WS+ query WS*                # spacedQueryLR
  | query WS+                    # spacedQueryR
  | '(' query ')'                # groupedQuery
  | NOT query                    # notQuery
  | query LOGICAL_OPERATOR query # operationQuery
  | expr RELATIONS expr          # relationExpr
  ;

funcCall: ID '(' ((expr|query) (',' (expr|query))*)? ')';

expr: funcCall
  | ID
  | value
  | WS+ expr WS*
  | expr WS+
  | '(' expr ')'
  | expr ARITIMETIC_OPERATORS expr
  ;

tuple: '(' exprSeq? ')';
list: '[' exprSeq? ']';
set: '{' exprSeq '}' | 'set' '(' ')';
dict: '{' (dictEntry (',' dictEntry)*)? '}';

dictEntry: WS* unhashable WS* ':' WS* expr WS*;
unhashable: STRING
  | NUMBER
  | BOOLEAN
  | NULL
  | tuple
  ;

exprSeq: expr WS* (',' WS* expr)* ','?;


value: NULL # null
  | STRING  # string
  | NUMBER  # number
  | list    # valueList
  | tuple   # valueTuple
  | dict    # valueDict
  | set     # valueSet
  ;

// def f(x:int,y):
//     return None
// def f(x:int,y:int):
//     return None
// def f(x:int=1,y:int=2):
//     return None
// def f(x=1,y=2):
//     return None