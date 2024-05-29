parser grammar PythonParser;

options {
  tokenVocab = PythonLexer;
}

code: (stat | '\n')* EOF;

stat: stat_possibility '\n'?;

stat_possibility: func
  | expr 
  | query
  | assignment
  ;

func: 'def' SPACE+ ID '(' params? ')' SPACE* ':' '\n' (TAB+ stat)* TAB+ 'return' SPACE+ expr? '\n';

params: param_case (',' param_case)*;

param_case: ID param_typed param_default?;
param_typed: ':' type;
param_default: '=' expr;

// func: 'def' SPACE+ ID '(' params? ')' SPACE* ':' '\n' (TAB+ stat)* TAB+ 'return' SPACE+ expr? '\n';

// params: param (',' param)*;

// param: ID (':' type)? ('=' expr);

type: 'int' | 'float' | 'str' | 'bool' 
  | 'None' | 'dict' | 'list' | 'tuple'
  | 'function' | 'object';

assignment: ID SPACE* '=' SPACE* (expr | query);

query: BOOLEAN                   # boolean
  | SPACE+ query SPACE+          # spaced_queryLR
  | SPACE+ query                 # spaced_queryL
  | query SPACE+                 # spaced_queryR
  | '(' query ')'                # parenQuery
  | NOT query                    # notQuery
  | query LOGICAL_OPERATOR query # logicalQuery
  | expr RELATIONS expr          # compareExpr
  ;

funcCall: ID '(' ((expr|query) (',' (expr|query))*)? ')';

expr: ID
  | value
  | SPACE+ expr SPACE+
  | SPACE+ expr
  | expr SPACE+
  | '(' expr ')'
  | expr ARITIMETIC_OPERATORS expr
  ;

value: NULL    # null
  | STRING     # string
  | NUMBER     # number
  ;

// def f(x:int,y):
//     return None
// def f(x:int,y:int):
//     return None
// def f(x:int=1,y:int=2):
//     return None
// def f(x=1,y=2):
//     return None