import sys

sys.path.append('./generated')

from antlr4 import *
from generated.grammar.TuneScriptVisitor import TuneScriptVisitor
from generated.grammar.TuneScriptParser import TuneScriptParser
from src.ast_nodes import *


class AstBuilder(TuneScriptVisitor):

    # S -> G K
    def visitTune(self, ctx: TuneScriptParser.TuneContext):
        globals_list = self.visit(ctx.globalSettings())
        tracks_list = self.visit(ctx.trackList())
        return Tune(globals_list, tracks_list)

    # G -> T G | ε
    def visitGlobalSettings(self, ctx: TuneScriptParser.GlobalSettingsContext):
        settings = []
        for setting_ctx in ctx.globalSetting():
            result = self.visit(setting_ctx)
            if result:
                settings.append(result)
        return settings

    # T -> tempo = number | ticks = number | time = number / number
    def visitGlobalSetting(self, ctx: TuneScriptParser.GlobalSettingContext):
        line = ctx.start.line

        if ctx.TEMPO():
            key = 'tempo'
            value = float(ctx.NUMBER().getText())
            return GlobalSetting(key, value, line)
        elif ctx.TICKS():
            key = 'ticks'
            value = float(ctx.NUMBER().getText())
            return GlobalSetting(key, value, line)
        elif ctx.TIME():
            # Obsługa timeSignature
            ts_ctx = ctx.timeSignature()
            num = int(ts_ctx.NUMBER(0).getText())
            den = int(ts_ctx.NUMBER(1).getText())
            return TimeSignatureSetting(num, den, line)

        return None

    # K -> I K | I
    def visitTrackList(self, ctx: TuneScriptParser.TrackListContext):
        tracks = []
        for track_ctx in ctx.trackDefinition():
            tracks.append(self.visit(track_ctx))
        return tracks

    # I -> track "id" { B }
    def visitTrackDefinition(self, ctx: TuneScriptParser.TrackDefinitionContext):
        name = ctx.STRING().getText().strip('"')
        track_body = self.visit(ctx.trackBody())
        line = ctx.start.line
        return Track(name, track_body['instrument'], track_body['commands'], line)

    # B -> J C
    def visitTrackBody(self, ctx: TuneScriptParser.TrackBodyContext):
        instrument = None
        # J
        if ctx.instrumentSetting():
            instrument = self.visit(ctx.instrumentSetting())

        # C (commandList)
        commands = self.visit(ctx.commandList())

        return {'instrument': instrument, 'commands': commands}

    # J -> instrument = id | ε
    def visitInstrumentSetting(self, ctx: TuneScriptParser.InstrumentSettingContext):
        name = ctx.ID().getText()
        line = ctx.start.line
        return InstrumentSetting(name, line)

    # C -> E C | E
    def visitCommandList(self, ctx: TuneScriptParser.CommandListContext):
        commands = []
        for cmd_ctx in ctx.command():
            cmd = self.visit(cmd_ctx)
            if cmd is not None:
                commands.append(cmd)
        return commands

    # E -> N | A | R
    def visitCommand(self, ctx: TuneScriptParser.CommandContext):
        if ctx.note():
            return self.visit(ctx.note())
        if ctx.chord():
            return self.visit(ctx.chord())
        if ctx.rest():
            return self.visit(ctx.rest())
        return None

    # N -> play H D
    def visitNote(self, ctx: TuneScriptParser.NoteContext):
        pitch = self.visit(ctx.pitch())
        duration = self.visit(ctx.duration())
        line = ctx.start.line
        return Note(pitch, duration, line)

    # A -> play < L > D
    def visitChord(self, ctx: TuneScriptParser.ChordContext):
        pitches = self.visit(ctx.pitchList())
        duration = self.visit(ctx.duration())
        line = ctx.start.line
        return Chord(pitches, duration, line)

    # R -> rest D
    def visitRest(self, ctx: TuneScriptParser.RestContext):
        duration = self.visit(ctx.duration())
        line = ctx.start.line
        return Rest(duration, line)

    # D -> for number beat | for number beats
    def visitDuration(self, ctx: TuneScriptParser.DurationContext):
        value = float(ctx.NUMBER().getText())
        line = ctx.start.line
        return Duration(value, line)

    # L -> H L | H
    def visitPitchList(self, ctx: TuneScriptParser.PitchListContext):
        pitches = []
        for pitch_ctx in ctx.pitch():
            pitches.append(self.visit(pitch_ctx))
        return pitches

    # H -> P number
    def visitPitch(self, ctx: TuneScriptParser.PitchContext):
        pitch_name_ctx = ctx.pitchName()

        note_letter = pitch_name_ctx.NOTE_LETTER().getText()
        octave = int(ctx.NUMBER().getText())

        accidental = None
        if pitch_name_ctx.SHARP():
            accidental = 'sharp'
        elif pitch_name_ctx.FLAT():
            accidental = 'flat'

        line = ctx.start.line
        return Pitch(note_letter, accidental, octave, line)