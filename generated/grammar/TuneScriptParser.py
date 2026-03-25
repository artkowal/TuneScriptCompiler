# Generated from grammar/TuneScript.g4 by ANTLR 4.13.2
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
        4,1,24,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,3,
        1,3,1,3,1,3,1,4,4,4,61,8,4,11,4,12,4,62,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,3,6,72,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,4,8,81,8,8,11,8,12,8,
        82,1,9,1,9,1,9,3,9,88,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,4,14,108,8,14,
        11,14,12,14,109,1,15,1,15,1,15,1,16,1,16,3,16,117,8,16,1,16,0,0,
        17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,2,1,0,10,11,1,
        0,12,13,111,0,34,1,0,0,0,2,41,1,0,0,0,4,53,1,0,0,0,6,55,1,0,0,0,
        8,60,1,0,0,0,10,64,1,0,0,0,12,71,1,0,0,0,14,75,1,0,0,0,16,80,1,0,
        0,0,18,87,1,0,0,0,20,89,1,0,0,0,22,93,1,0,0,0,24,99,1,0,0,0,26,102,
        1,0,0,0,28,107,1,0,0,0,30,111,1,0,0,0,32,114,1,0,0,0,34,35,3,2,1,
        0,35,36,3,8,4,0,36,37,5,0,0,1,37,1,1,0,0,0,38,40,3,4,2,0,39,38,1,
        0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,
        41,1,0,0,0,44,45,5,2,0,0,45,46,5,15,0,0,46,54,5,21,0,0,47,48,5,3,
        0,0,48,49,5,15,0,0,49,54,5,21,0,0,50,51,5,4,0,0,51,52,5,15,0,0,52,
        54,3,6,3,0,53,44,1,0,0,0,53,47,1,0,0,0,53,50,1,0,0,0,54,5,1,0,0,
        0,55,56,5,21,0,0,56,57,5,1,0,0,57,58,5,21,0,0,58,7,1,0,0,0,59,61,
        3,10,5,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,9,1,0,0,0,64,65,5,5,0,0,65,66,5,22,0,0,66,67,5,16,0,0,67,68,3,
        12,6,0,68,69,5,17,0,0,69,11,1,0,0,0,70,72,3,14,7,0,71,70,1,0,0,0,
        71,72,1,0,0,0,72,73,1,0,0,0,73,74,3,16,8,0,74,13,1,0,0,0,75,76,5,
        6,0,0,76,77,5,15,0,0,77,78,5,20,0,0,78,15,1,0,0,0,79,81,3,18,9,0,
        80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,17,1,
        0,0,0,84,88,3,20,10,0,85,88,3,22,11,0,86,88,3,24,12,0,87,84,1,0,
        0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,19,1,0,0,0,89,90,5,7,0,0,90,91,
        3,30,15,0,91,92,3,26,13,0,92,21,1,0,0,0,93,94,5,7,0,0,94,95,5,18,
        0,0,95,96,3,28,14,0,96,97,5,19,0,0,97,98,3,26,13,0,98,23,1,0,0,0,
        99,100,5,8,0,0,100,101,3,26,13,0,101,25,1,0,0,0,102,103,5,9,0,0,
        103,104,5,21,0,0,104,105,7,0,0,0,105,27,1,0,0,0,106,108,3,30,15,
        0,107,106,1,0,0,0,108,109,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,
        0,110,29,1,0,0,0,111,112,3,32,16,0,112,113,5,21,0,0,113,31,1,0,0,
        0,114,116,5,14,0,0,115,117,7,1,0,0,116,115,1,0,0,0,116,117,1,0,0,
        0,117,33,1,0,0,0,8,41,53,62,71,82,87,109,116
    ]

class TuneScriptParser ( Parser ):

    grammarFileName = "TuneScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'tempo'", "'ticks'", "'time'", 
                     "'track'", "'instrument'", "'play'", "'rest'", "'for'", 
                     "'beat'", "'beats'", "'sharp'", "'flat'", "<INVALID>", 
                     "'='", "'{'", "'}'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TEMPO", "TICKS", "TIME", 
                      "TRACK", "INSTRUMENT", "PLAY", "REST", "FOR", "BEAT", 
                      "BEATS", "SHARP", "FLAT", "NOTE_LETTER", "EQ", "LBRACE", 
                      "RBRACE", "L_ANGLE", "R_ANGLE", "ID", "NUMBER", "STRING", 
                      "WS", "LINE_COMMENT" ]

    RULE_tune = 0
    RULE_globalSettings = 1
    RULE_globalSetting = 2
    RULE_timeSignature = 3
    RULE_trackList = 4
    RULE_trackDefinition = 5
    RULE_trackBody = 6
    RULE_instrumentSetting = 7
    RULE_commandList = 8
    RULE_command = 9
    RULE_note = 10
    RULE_chord = 11
    RULE_rest = 12
    RULE_duration = 13
    RULE_pitchList = 14
    RULE_pitch = 15
    RULE_pitchName = 16

    ruleNames =  [ "tune", "globalSettings", "globalSetting", "timeSignature", 
                   "trackList", "trackDefinition", "trackBody", "instrumentSetting", 
                   "commandList", "command", "note", "chord", "rest", "duration", 
                   "pitchList", "pitch", "pitchName" ]

    EOF = Token.EOF
    T__0=1
    TEMPO=2
    TICKS=3
    TIME=4
    TRACK=5
    INSTRUMENT=6
    PLAY=7
    REST=8
    FOR=9
    BEAT=10
    BEATS=11
    SHARP=12
    FLAT=13
    NOTE_LETTER=14
    EQ=15
    LBRACE=16
    RBRACE=17
    L_ANGLE=18
    R_ANGLE=19
    ID=20
    NUMBER=21
    STRING=22
    WS=23
    LINE_COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TuneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalSettings(self):
            return self.getTypedRuleContext(TuneScriptParser.GlobalSettingsContext,0)


        def trackList(self):
            return self.getTypedRuleContext(TuneScriptParser.TrackListContext,0)


        def EOF(self):
            return self.getToken(TuneScriptParser.EOF, 0)

        def getRuleIndex(self):
            return TuneScriptParser.RULE_tune

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTune" ):
                listener.enterTune(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTune" ):
                listener.exitTune(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTune" ):
                return visitor.visitTune(self)
            else:
                return visitor.visitChildren(self)




    def tune(self):

        localctx = TuneScriptParser.TuneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tune)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.globalSettings()
            self.state = 35
            self.trackList()
            self.state = 36
            self.match(TuneScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalSettingsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalSetting(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuneScriptParser.GlobalSettingContext)
            else:
                return self.getTypedRuleContext(TuneScriptParser.GlobalSettingContext,i)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_globalSettings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalSettings" ):
                listener.enterGlobalSettings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalSettings" ):
                listener.exitGlobalSettings(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalSettings" ):
                return visitor.visitGlobalSettings(self)
            else:
                return visitor.visitChildren(self)




    def globalSettings(self):

        localctx = TuneScriptParser.GlobalSettingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globalSettings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 38
                self.globalSetting()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalSettingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMPO(self):
            return self.getToken(TuneScriptParser.TEMPO, 0)

        def EQ(self):
            return self.getToken(TuneScriptParser.EQ, 0)

        def NUMBER(self):
            return self.getToken(TuneScriptParser.NUMBER, 0)

        def TICKS(self):
            return self.getToken(TuneScriptParser.TICKS, 0)

        def TIME(self):
            return self.getToken(TuneScriptParser.TIME, 0)

        def timeSignature(self):
            return self.getTypedRuleContext(TuneScriptParser.TimeSignatureContext,0)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_globalSetting

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalSetting" ):
                listener.enterGlobalSetting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalSetting" ):
                listener.exitGlobalSetting(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalSetting" ):
                return visitor.visitGlobalSetting(self)
            else:
                return visitor.visitChildren(self)




    def globalSetting(self):

        localctx = TuneScriptParser.GlobalSettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_globalSetting)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(TuneScriptParser.TEMPO)
                self.state = 45
                self.match(TuneScriptParser.EQ)
                self.state = 46
                self.match(TuneScriptParser.NUMBER)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(TuneScriptParser.TICKS)
                self.state = 48
                self.match(TuneScriptParser.EQ)
                self.state = 49
                self.match(TuneScriptParser.NUMBER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(TuneScriptParser.TIME)
                self.state = 51
                self.match(TuneScriptParser.EQ)
                self.state = 52
                self.timeSignature()
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


    class TimeSignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(TuneScriptParser.NUMBER)
            else:
                return self.getToken(TuneScriptParser.NUMBER, i)

        def getRuleIndex(self):
            return TuneScriptParser.RULE_timeSignature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeSignature" ):
                listener.enterTimeSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeSignature" ):
                listener.exitTimeSignature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeSignature" ):
                return visitor.visitTimeSignature(self)
            else:
                return visitor.visitChildren(self)




    def timeSignature(self):

        localctx = TuneScriptParser.TimeSignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_timeSignature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(TuneScriptParser.NUMBER)
            self.state = 56
            self.match(TuneScriptParser.T__0)
            self.state = 57
            self.match(TuneScriptParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrackListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trackDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuneScriptParser.TrackDefinitionContext)
            else:
                return self.getTypedRuleContext(TuneScriptParser.TrackDefinitionContext,i)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_trackList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrackList" ):
                listener.enterTrackList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrackList" ):
                listener.exitTrackList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrackList" ):
                return visitor.visitTrackList(self)
            else:
                return visitor.visitChildren(self)




    def trackList(self):

        localctx = TuneScriptParser.TrackListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_trackList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.trackDefinition()
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrackDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRACK(self):
            return self.getToken(TuneScriptParser.TRACK, 0)

        def STRING(self):
            return self.getToken(TuneScriptParser.STRING, 0)

        def LBRACE(self):
            return self.getToken(TuneScriptParser.LBRACE, 0)

        def trackBody(self):
            return self.getTypedRuleContext(TuneScriptParser.TrackBodyContext,0)


        def RBRACE(self):
            return self.getToken(TuneScriptParser.RBRACE, 0)

        def getRuleIndex(self):
            return TuneScriptParser.RULE_trackDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrackDefinition" ):
                listener.enterTrackDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrackDefinition" ):
                listener.exitTrackDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrackDefinition" ):
                return visitor.visitTrackDefinition(self)
            else:
                return visitor.visitChildren(self)




    def trackDefinition(self):

        localctx = TuneScriptParser.TrackDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_trackDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(TuneScriptParser.TRACK)
            self.state = 65
            self.match(TuneScriptParser.STRING)
            self.state = 66
            self.match(TuneScriptParser.LBRACE)
            self.state = 67
            self.trackBody()
            self.state = 68
            self.match(TuneScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrackBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commandList(self):
            return self.getTypedRuleContext(TuneScriptParser.CommandListContext,0)


        def instrumentSetting(self):
            return self.getTypedRuleContext(TuneScriptParser.InstrumentSettingContext,0)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_trackBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrackBody" ):
                listener.enterTrackBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrackBody" ):
                listener.exitTrackBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrackBody" ):
                return visitor.visitTrackBody(self)
            else:
                return visitor.visitChildren(self)




    def trackBody(self):

        localctx = TuneScriptParser.TrackBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_trackBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 70
                self.instrumentSetting()


            self.state = 73
            self.commandList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrumentSettingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTRUMENT(self):
            return self.getToken(TuneScriptParser.INSTRUMENT, 0)

        def EQ(self):
            return self.getToken(TuneScriptParser.EQ, 0)

        def ID(self):
            return self.getToken(TuneScriptParser.ID, 0)

        def getRuleIndex(self):
            return TuneScriptParser.RULE_instrumentSetting

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrumentSetting" ):
                listener.enterInstrumentSetting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrumentSetting" ):
                listener.exitInstrumentSetting(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrumentSetting" ):
                return visitor.visitInstrumentSetting(self)
            else:
                return visitor.visitChildren(self)




    def instrumentSetting(self):

        localctx = TuneScriptParser.InstrumentSettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instrumentSetting)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(TuneScriptParser.INSTRUMENT)
            self.state = 76
            self.match(TuneScriptParser.EQ)
            self.state = 77
            self.match(TuneScriptParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuneScriptParser.CommandContext)
            else:
                return self.getTypedRuleContext(TuneScriptParser.CommandContext,i)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_commandList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandList" ):
                listener.enterCommandList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandList" ):
                listener.exitCommandList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandList" ):
                return visitor.visitCommandList(self)
            else:
                return visitor.visitChildren(self)




    def commandList(self):

        localctx = TuneScriptParser.CommandListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_commandList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.command()
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7 or _la==8):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note(self):
            return self.getTypedRuleContext(TuneScriptParser.NoteContext,0)


        def chord(self):
            return self.getTypedRuleContext(TuneScriptParser.ChordContext,0)


        def rest(self):
            return self.getTypedRuleContext(TuneScriptParser.RestContext,0)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = TuneScriptParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_command)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.note()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.chord()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.rest()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAY(self):
            return self.getToken(TuneScriptParser.PLAY, 0)

        def pitch(self):
            return self.getTypedRuleContext(TuneScriptParser.PitchContext,0)


        def duration(self):
            return self.getTypedRuleContext(TuneScriptParser.DurationContext,0)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNote" ):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)




    def note(self):

        localctx = TuneScriptParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(TuneScriptParser.PLAY)
            self.state = 90
            self.pitch()
            self.state = 91
            self.duration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAY(self):
            return self.getToken(TuneScriptParser.PLAY, 0)

        def L_ANGLE(self):
            return self.getToken(TuneScriptParser.L_ANGLE, 0)

        def pitchList(self):
            return self.getTypedRuleContext(TuneScriptParser.PitchListContext,0)


        def R_ANGLE(self):
            return self.getToken(TuneScriptParser.R_ANGLE, 0)

        def duration(self):
            return self.getTypedRuleContext(TuneScriptParser.DurationContext,0)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_chord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChord" ):
                listener.enterChord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChord" ):
                listener.exitChord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChord" ):
                return visitor.visitChord(self)
            else:
                return visitor.visitChildren(self)




    def chord(self):

        localctx = TuneScriptParser.ChordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_chord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(TuneScriptParser.PLAY)
            self.state = 94
            self.match(TuneScriptParser.L_ANGLE)
            self.state = 95
            self.pitchList()
            self.state = 96
            self.match(TuneScriptParser.R_ANGLE)
            self.state = 97
            self.duration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REST(self):
            return self.getToken(TuneScriptParser.REST, 0)

        def duration(self):
            return self.getTypedRuleContext(TuneScriptParser.DurationContext,0)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRest" ):
                listener.enterRest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRest" ):
                listener.exitRest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRest" ):
                return visitor.visitRest(self)
            else:
                return visitor.visitChildren(self)




    def rest(self):

        localctx = TuneScriptParser.RestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_rest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(TuneScriptParser.REST)
            self.state = 100
            self.duration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TuneScriptParser.FOR, 0)

        def NUMBER(self):
            return self.getToken(TuneScriptParser.NUMBER, 0)

        def BEAT(self):
            return self.getToken(TuneScriptParser.BEAT, 0)

        def BEATS(self):
            return self.getToken(TuneScriptParser.BEATS, 0)

        def getRuleIndex(self):
            return TuneScriptParser.RULE_duration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDuration" ):
                listener.enterDuration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDuration" ):
                listener.exitDuration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDuration" ):
                return visitor.visitDuration(self)
            else:
                return visitor.visitChildren(self)




    def duration(self):

        localctx = TuneScriptParser.DurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_duration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(TuneScriptParser.FOR)
            self.state = 103
            self.match(TuneScriptParser.NUMBER)
            self.state = 104
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PitchListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pitch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuneScriptParser.PitchContext)
            else:
                return self.getTypedRuleContext(TuneScriptParser.PitchContext,i)


        def getRuleIndex(self):
            return TuneScriptParser.RULE_pitchList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPitchList" ):
                listener.enterPitchList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPitchList" ):
                listener.exitPitchList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPitchList" ):
                return visitor.visitPitchList(self)
            else:
                return visitor.visitChildren(self)




    def pitchList(self):

        localctx = TuneScriptParser.PitchListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_pitchList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.pitch()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PitchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pitchName(self):
            return self.getTypedRuleContext(TuneScriptParser.PitchNameContext,0)


        def NUMBER(self):
            return self.getToken(TuneScriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return TuneScriptParser.RULE_pitch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPitch" ):
                listener.enterPitch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPitch" ):
                listener.exitPitch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPitch" ):
                return visitor.visitPitch(self)
            else:
                return visitor.visitChildren(self)




    def pitch(self):

        localctx = TuneScriptParser.PitchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pitch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.pitchName()
            self.state = 112
            self.match(TuneScriptParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PitchNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTE_LETTER(self):
            return self.getToken(TuneScriptParser.NOTE_LETTER, 0)

        def SHARP(self):
            return self.getToken(TuneScriptParser.SHARP, 0)

        def FLAT(self):
            return self.getToken(TuneScriptParser.FLAT, 0)

        def getRuleIndex(self):
            return TuneScriptParser.RULE_pitchName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPitchName" ):
                listener.enterPitchName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPitchName" ):
                listener.exitPitchName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPitchName" ):
                return visitor.visitPitchName(self)
            else:
                return visitor.visitChildren(self)




    def pitchName(self):

        localctx = TuneScriptParser.PitchNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pitchName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(TuneScriptParser.NOTE_LETTER)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==13:
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





