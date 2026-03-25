# Generated from grammar/TuneScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TuneScriptParser import TuneScriptParser
else:
    from TuneScriptParser import TuneScriptParser

# This class defines a complete generic visitor for a parse tree produced by TuneScriptParser.

class TuneScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TuneScriptParser#tune.
    def visitTune(self, ctx:TuneScriptParser.TuneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#globalSettings.
    def visitGlobalSettings(self, ctx:TuneScriptParser.GlobalSettingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#globalSetting.
    def visitGlobalSetting(self, ctx:TuneScriptParser.GlobalSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#timeSignature.
    def visitTimeSignature(self, ctx:TuneScriptParser.TimeSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#trackList.
    def visitTrackList(self, ctx:TuneScriptParser.TrackListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#trackDefinition.
    def visitTrackDefinition(self, ctx:TuneScriptParser.TrackDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#trackBody.
    def visitTrackBody(self, ctx:TuneScriptParser.TrackBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#instrumentSetting.
    def visitInstrumentSetting(self, ctx:TuneScriptParser.InstrumentSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#commandList.
    def visitCommandList(self, ctx:TuneScriptParser.CommandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#command.
    def visitCommand(self, ctx:TuneScriptParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#note.
    def visitNote(self, ctx:TuneScriptParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#chord.
    def visitChord(self, ctx:TuneScriptParser.ChordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#rest.
    def visitRest(self, ctx:TuneScriptParser.RestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#duration.
    def visitDuration(self, ctx:TuneScriptParser.DurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#pitchList.
    def visitPitchList(self, ctx:TuneScriptParser.PitchListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#pitch.
    def visitPitch(self, ctx:TuneScriptParser.PitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuneScriptParser#pitchName.
    def visitPitchName(self, ctx:TuneScriptParser.PitchNameContext):
        return self.visitChildren(ctx)



del TuneScriptParser