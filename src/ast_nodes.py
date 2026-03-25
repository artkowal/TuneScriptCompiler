class Tune:
    """Główna klasa, reprezentująca cały plik .tune"""

    def __init__(self, global_settings, tracks):
        self.global_settings = global_settings  # Lista obiektów GlobalSetting
        self.tracks = tracks  # Lista obiektów Track

    def __repr__(self):
        return f"Tune(globals={self.global_settings}, tracks={self.tracks})"


class GlobalSetting:
    """Reprezentuje 'tempo = 120' lub 'ticks = 480'"""

    def __init__(self, key, value, line):
        self.key = key  # str: 'tempo' lub 'ticks'
        self.value = value  # float
        self.line = line  # int: numer linii

    def __repr__(self):
        return f"GlobalSetting(line={self.line}, key='{self.key}', value={self.value})"


class TimeSignatureSetting:
    """Reprezentuje 'time = 3/4'"""

    def __init__(self, numerator, denominator, line):
        self.numerator = numerator  # int: 3
        self.denominator = denominator  # int: 4
        self.line = line

    def __repr__(self):
        return f"TimeSignature(line={self.line}, value={self.numerator}/{self.denominator})"


class Track:
    """Reprezentuje jeden 'track "Nazwa" { ... }'"""

    def __init__(self, name, instrument, commands, line):
        self.name = name  # str: "Nazwa"
        self.instrument = instrument  # obiekt InstrumentSetting lub None
        self.commands = commands  # Lista obiektów (Note, Chord, Rest)
        self.line = line

    def __repr__(self):
        return f"\n  Track(line={self.line}, name='{self.name}', instrument={self.instrument}, commands={self.commands})"


class InstrumentSetting:
    """Reprezentuje 'instrument = piano'"""

    def __init__(self, name, line):
        self.name = name  # str: 'piano'
        self.line = line

    def __repr__(self):
        return f"Instrument(line={self.line}, name='{self.name}')"


class Note:
    """Reprezentuje 'play c#4 for 1 beat'"""

    def __init__(self, pitch, duration, line):
        self.pitch = pitch  # obiekt Pitch
        self.duration = duration  # obiekt Duration
        self.line = line

    def __repr__(self):
        return f"\n    Note(line={self.line}, pitch={self.pitch}, duration={self.duration})"


class Chord:
    """Reprezentuje 'play <c4 e4 g4> for 1 beat'"""

    def __init__(self, pitches, duration, line):
        self.pitches = pitches  # Lista obiektów Pitch
        self.duration = duration  # obiekt Duration
        self.line = line

    def __repr__(self):
        return f"\n    Chord(line={self.line}, pitches={self.pitches}, duration={self.duration})"


class Rest:
    """Reprezentuje 'rest for 1 beat'"""

    def __init__(self, duration, line):
        self.duration = duration  # obiekt Duration
        self.line = line

    def __repr__(self):
        return f"\n    Rest(line={self.line}, duration={self.duration})"


class Duration:
    """Reprezentuje 'for 1.5 beats'"""

    def __init__(self, value, line):
        self.value = value  # float: 1.5
        self.line = line

    def __repr__(self):
        return f"Duration(line={self.line}, value={self.value})"


class Pitch:
    """Reprezentuje 'c#4'"""

    def __init__(self, note_letter, accidental, octave, line):
        self.note_letter = note_letter  # str: 'c'
        self.accidental = accidental  # str: 'sharp' lub 'flat' lub None
        self.octave = octave  # int: 4
        self.line = line

    def __repr__(self):
        acc = f"'{self.accidental}'" if self.accidental else "None"
        return f"Pitch(line={self.line}, note='{self.note_letter}', acc={acc}, octave={self.octave})"