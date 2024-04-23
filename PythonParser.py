# Generated from PythonParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,4,3,47,8,3,11,3,12,3,48,1,3,1,3,5,3,53,8,3,10,
        3,12,3,56,9,3,3,3,58,8,3,1,3,1,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,
        1,4,1,4,5,4,70,8,4,10,4,12,4,73,9,4,1,5,1,5,5,5,77,8,5,10,5,12,5,
        80,9,5,1,5,1,5,5,5,84,8,5,10,5,12,5,87,9,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,102,8,6,1,6,1,6,1,6,5,6,107,8,
        6,10,6,12,6,110,9,6,1,7,1,7,1,7,1,7,3,7,116,8,7,1,7,0,2,6,12,8,0,
        2,4,6,8,10,12,14,0,1,1,0,1,2,129,0,16,1,0,0,0,2,30,1,0,0,0,4,35,
        1,0,0,0,6,57,1,0,0,0,8,67,1,0,0,0,10,74,1,0,0,0,12,101,1,0,0,0,14,
        115,1,0,0,0,16,21,3,2,1,0,17,18,5,1,0,0,18,20,3,2,1,0,19,17,1,0,
        0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,
        1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,31,3,4,2,0,27,31,3,6,3,0,28,
        31,3,10,5,0,29,31,3,8,4,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,
        0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,34,5,1,0,0,33,32,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,35,1,0,0,0,38,
        39,6,3,-1,0,39,58,5,32,0,0,40,58,3,14,7,0,41,42,5,17,0,0,42,43,3,
        6,3,0,43,44,5,18,0,0,44,58,1,0,0,0,45,47,5,4,0,0,46,45,1,0,0,0,47,
        48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,54,3,6,3,
        0,51,53,5,4,0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,
        1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,57,38,1,0,0,0,57,40,1,0,0,0,
        57,41,1,0,0,0,57,46,1,0,0,0,58,64,1,0,0,0,59,60,10,3,0,0,60,61,5,
        13,0,0,61,63,3,6,3,4,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,
        65,1,0,0,0,65,7,1,0,0,0,66,64,1,0,0,0,67,71,5,28,0,0,68,70,8,0,0,
        0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,9,1,
        0,0,0,73,71,1,0,0,0,74,78,5,32,0,0,75,77,5,4,0,0,76,75,1,0,0,0,77,
        80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,
        0,81,85,5,24,0,0,82,84,5,4,0,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,
        1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,3,6,3,0,
        89,11,1,0,0,0,90,91,6,6,-1,0,91,92,5,17,0,0,92,93,3,12,6,0,93,94,
        5,18,0,0,94,102,1,0,0,0,95,96,5,15,0,0,96,102,3,12,6,3,97,98,3,6,
        3,0,98,99,5,16,0,0,99,100,3,6,3,0,100,102,1,0,0,0,101,90,1,0,0,0,
        101,95,1,0,0,0,101,97,1,0,0,0,102,108,1,0,0,0,103,104,10,2,0,0,104,
        105,5,29,0,0,105,107,3,12,6,3,106,103,1,0,0,0,107,110,1,0,0,0,108,
        106,1,0,0,0,108,109,1,0,0,0,109,13,1,0,0,0,110,108,1,0,0,0,111,116,
        5,31,0,0,112,116,5,30,0,0,113,116,5,34,0,0,114,116,5,35,0,0,115,
        111,1,0,0,0,115,112,1,0,0,0,115,113,1,0,0,0,115,114,1,0,0,0,116,
        15,1,0,0,0,13,21,30,35,48,54,57,64,71,78,85,101,108,115
    ]

class PythonParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "'\\r'", "'\\t'", "' '", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'**'", "'<<'", "'>>'", 
                     "<INVALID>", "'lambda'", "'not'", "<INVALID>", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "'='", "'.'", 
                     "':'", "';'", "'#'", "<INVALID>", "'None'" ]

    symbolicNames = [ "<INVALID>", "LINE_BREAK", "BEGIN_LINE", "TAB", "SPACE", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "POW", "LSHIFT", 
                      "RSHIFT", "ARITIMETIC_OPERATORS", "LAMBDA", "NOT", 
                      "RELATIONS", "LPARENTHESIS", "RPARENTHESIS", "LBRACKET", 
                      "RBRACKET", "LBRACE", "RBRACE", "COMMA", "ASSIGN", 
                      "DOT", "COLON", "SEMI", "HASH", "LOGICAL_OPERATOR", 
                      "NULL", "BOOLEAN", "ID", "INDENT", "STRING", "NUMBER", 
                      "EXP", "WS" ]

    RULE_start = 0
    RULE_code = 1
    RULE_emptyLine = 2
    RULE_expr = 3
    RULE_comment = 4
    RULE_assignment = 5
    RULE_query = 6
    RULE_value = 7

    ruleNames =  [ "start", "code", "emptyLine", "expr", "comment", "assignment", 
                   "query", "value" ]

    EOF = Token.EOF
    LINE_BREAK=1
    BEGIN_LINE=2
    TAB=3
    SPACE=4
    ADD=5
    SUB=6
    MUL=7
    DIV=8
    MOD=9
    POW=10
    LSHIFT=11
    RSHIFT=12
    ARITIMETIC_OPERATORS=13
    LAMBDA=14
    NOT=15
    RELATIONS=16
    LPARENTHESIS=17
    RPARENTHESIS=18
    LBRACKET=19
    RBRACKET=20
    LBRACE=21
    RBRACE=22
    COMMA=23
    ASSIGN=24
    DOT=25
    COLON=26
    SEMI=27
    HASH=28
    LOGICAL_OPERATOR=29
    NULL=30
    BOOLEAN=31
    ID=32
    INDENT=33
    STRING=34
    NUMBER=35
    EXP=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.CodeContext)
            else:
                return self.getTypedRuleContext(PythonParser.CodeContext,i)


        def EOF(self):
            return self.getToken(PythonParser.EOF, 0)

        def LINE_BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.LINE_BREAK)
            else:
                return self.getToken(PythonParser.LINE_BREAK, i)

        def getRuleIndex(self):
            return PythonParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = PythonParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.code()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 17
                self.match(PythonParser.LINE_BREAK)
                self.state = 18
                self.code()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(PythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def emptyLine(self):
            return self.getTypedRuleContext(PythonParser.EmptyLineContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PythonParser.AssignmentContext,0)


        def comment(self):
            return self.getTypedRuleContext(PythonParser.CommentContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_code

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = PythonParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_code)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.emptyLine()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.LINE_BREAK)
            else:
                return self.getToken(PythonParser.LINE_BREAK, i)

        def getRuleIndex(self):
            return PythonParser.RULE_emptyLine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyLine" ):
                return visitor.visitEmptyLine(self)
            else:
                return visitor.visitChildren(self)




    def emptyLine(self):

        localctx = PythonParser.EmptyLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_emptyLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 32
                    self.match(PythonParser.LINE_BREAK) 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(PythonParser.ValueContext,0)


        def LPARENTHESIS(self):
            return self.getToken(PythonParser.LPARENTHESIS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)


        def RPARENTHESIS(self):
            return self.getToken(PythonParser.RPARENTHESIS, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.SPACE)
            else:
                return self.getToken(PythonParser.SPACE, i)

        def ARITIMETIC_OPERATORS(self):
            return self.getToken(PythonParser.ARITIMETIC_OPERATORS, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.state = 39
                self.match(PythonParser.ID)
                pass
            elif token in [30, 31, 34, 35]:
                self.state = 40
                self.value()
                pass
            elif token in [17]:
                self.state = 41
                self.match(PythonParser.LPARENTHESIS)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(PythonParser.RPARENTHESIS)
                pass
            elif token in [4]:
                self.state = 46 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 45
                        self.match(PythonParser.SPACE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 48 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 50
                self.expr(0)
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 51
                        self.match(PythonParser.SPACE) 
                    self.state = 56
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 59
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 60
                    self.match(PythonParser.ARITIMETIC_OPERATORS)
                    self.state = 61
                    self.expr(4) 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(PythonParser.HASH, 0)

        def BEGIN_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.BEGIN_LINE)
            else:
                return self.getToken(PythonParser.BEGIN_LINE, i)

        def LINE_BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.LINE_BREAK)
            else:
                return self.getToken(PythonParser.LINE_BREAK, i)

        def getRuleIndex(self):
            return PythonParser.RULE_comment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = PythonParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(PythonParser.HASH)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274877906936) != 0):
                self.state = 68
                _la = self._input.LA(1)
                if _la <= 0 or _la==1 or _la==2:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(PythonParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.SPACE)
            else:
                return self.getToken(PythonParser.SPACE, i)

        def getRuleIndex(self):
            return PythonParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PythonParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(PythonParser.ID)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 75
                self.match(PythonParser.SPACE)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(PythonParser.ASSIGN)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.match(PythonParser.SPACE) 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 88
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CompareExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)

        def RELATIONS(self):
            return self.getToken(PythonParser.RELATIONS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExp" ):
                return visitor.visitCompareExp(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPARENTHESIS(self):
            return self.getToken(PythonParser.LPARENTHESIS, 0)
        def query(self):
            return self.getTypedRuleContext(PythonParser.QueryContext,0)

        def RPARENTHESIS(self):
            return self.getToken(PythonParser.RPARENTHESIS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExp" ):
                return visitor.visitParenExp(self)
            else:
                return visitor.visitChildren(self)


    class LogicalExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.QueryContext)
            else:
                return self.getTypedRuleContext(PythonParser.QueryContext,i)

        def LOGICAL_OPERATOR(self):
            return self.getToken(PythonParser.LOGICAL_OPERATOR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExp" ):
                return visitor.visitLogicalExp(self)
            else:
                return visitor.visitChildren(self)


    class NotExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PythonParser.NOT, 0)
        def query(self):
            return self.getTypedRuleContext(PythonParser.QueryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExp" ):
                return visitor.visitNotExp(self)
            else:
                return visitor.visitChildren(self)



    def query(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParser.QueryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_query, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = PythonParser.ParenExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 91
                self.match(PythonParser.LPARENTHESIS)
                self.state = 92
                self.query(0)
                self.state = 93
                self.match(PythonParser.RPARENTHESIS)
                pass

            elif la_ == 2:
                localctx = PythonParser.NotExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(PythonParser.NOT)
                self.state = 96
                self.query(3)
                pass

            elif la_ == 3:
                localctx = PythonParser.CompareExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.expr(0)
                self.state = 98
                self.match(PythonParser.RELATIONS)
                self.state = 99
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParser.LogicalExpContext(self, PythonParser.QueryContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_query)
                    self.state = 103
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 104
                    self.match(PythonParser.LOGICAL_OPERATOR)
                    self.state = 105
                    self.query(3) 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(PythonParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(PythonParser.BOOLEAN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class NullContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(PythonParser.NULL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull" ):
                return visitor.visitNull(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PythonParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = PythonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = PythonParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(PythonParser.BOOLEAN)
                pass
            elif token in [30]:
                localctx = PythonParser.NullContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(PythonParser.NULL)
                pass
            elif token in [34]:
                localctx = PythonParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(PythonParser.STRING)
                pass
            elif token in [35]:
                localctx = PythonParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(PythonParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        self._predicates[6] = self.query_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def query_sempred(self, localctx:QueryContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




