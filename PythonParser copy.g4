parser grammar PythonParser;

options {
  tokenVocab = PythonLexer;
}

start
  : code ('\n' code)* EOF
  ;

code
  : emptyLine
  | expr
  | assignment
  | comment
  //| query
  ;

emptyLine
  : '\n'*
  ;

expr
  : ID
  | value
  | expr ARITIMETIC_OPERATORS expr
  | '(' expr ')'
  | SPACE+ expr SPACE*
  ;

comment
  :  '#' ~( '\r' | '\n' )*
  ;

assignment
  : ID SPACE* '=' SPACE* expr
  ;

query
  : '(' query ')'                # parenExp
  | NOT query                    # notExp
  | query LOGICAL_OPERATOR query # logicalExp
  | expr RELATIONS expr          # compareExp
  ;

value
  : BOOLEAN # boolean
  | NULL    # null
  | STRING  # string
  | NUMBER  # number
  ;