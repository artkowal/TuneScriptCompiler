# Generated from grammar/TuneScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TuneScriptParser import TuneScriptParser
else:
    from TuneScriptParser import TuneScriptParser

# This class defines a complete listener for a parse tree produced by TuneScriptParser.
class TuneScriptListener(ParseTreeListener):

    # Enter a parse tree produced by TuneScriptParser#tune.
    def enterTune(self, ctx:TuneScriptParser.TuneContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#tune.
    def exitTune(self, ctx:TuneScriptParser.TuneContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#globalSettings.
    def enterGlobalSettings(self, ctx:TuneScriptParser.GlobalSettingsContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#globalSettings.
    def exitGlobalSettings(self, ctx:TuneScriptParser.GlobalSettingsContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#globalSetting.
    def enterGlobalSetting(self, ctx:TuneScriptParser.GlobalSettingContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#globalSetting.
    def exitGlobalSetting(self, ctx:TuneScriptParser.GlobalSettingContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#timeSignature.
    def enterTimeSignature(self, ctx:TuneScriptParser.TimeSignatureContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#timeSignature.
    def exitTimeSignature(self, ctx:TuneScriptParser.TimeSignatureContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#trackList.
    def enterTrackList(self, ctx:TuneScriptParser.TrackListContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#trackList.
    def exitTrackList(self, ctx:TuneScriptParser.TrackListContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#trackDefinition.
    def enterTrackDefinition(self, ctx:TuneScriptParser.TrackDefinitionContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#trackDefinition.
    def exitTrackDefinition(self, ctx:TuneScriptParser.TrackDefinitionContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#trackBody.
    def enterTrackBody(self, ctx:TuneScriptParser.TrackBodyContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#trackBody.
    def exitTrackBody(self, ctx:TuneScriptParser.TrackBodyContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#instrumentSetting.
    def enterInstrumentSetting(self, ctx:TuneScriptParser.InstrumentSettingContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#instrumentSetting.
    def exitInstrumentSetting(self, ctx:TuneScriptParser.InstrumentSettingContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#commandList.
    def enterCommandList(self, ctx:TuneScriptParser.CommandListContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#commandList.
    def exitCommandList(self, ctx:TuneScriptParser.CommandListContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#command.
    def enterCommand(self, ctx:TuneScriptParser.CommandContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#command.
    def exitCommand(self, ctx:TuneScriptParser.CommandContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#note.
    def enterNote(self, ctx:TuneScriptParser.NoteContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#note.
    def exitNote(self, ctx:TuneScriptParser.NoteContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#chord.
    def enterChord(self, ctx:TuneScriptParser.ChordContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#chord.
    def exitChord(self, ctx:TuneScriptParser.ChordContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#rest.
    def enterRest(self, ctx:TuneScriptParser.RestContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#rest.
    def exitRest(self, ctx:TuneScriptParser.RestContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#duration.
    def enterDuration(self, ctx:TuneScriptParser.DurationContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#duration.
    def exitDuration(self, ctx:TuneScriptParser.DurationContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#pitchList.
    def enterPitchList(self, ctx:TuneScriptParser.PitchListContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#pitchList.
    def exitPitchList(self, ctx:TuneScriptParser.PitchListContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#pitch.
    def enterPitch(self, ctx:TuneScriptParser.PitchContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#pitch.
    def exitPitch(self, ctx:TuneScriptParser.PitchContext):
        pass


    # Enter a parse tree produced by TuneScriptParser#pitchName.
    def enterPitchName(self, ctx:TuneScriptParser.PitchNameContext):
        pass

    # Exit a parse tree produced by TuneScriptParser#pitchName.
    def exitPitchName(self, ctx:TuneScriptParser.PitchNameContext):
        pass



del TuneScriptParser