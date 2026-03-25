from src.ast_nodes import *
from src.semantic_analyzer import CompilationContext, INSTRUMENT_MAP

# --- Stałe do konwersji nut ---
NOTE_OFFSETS = {
    'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11
}


def pitch_to_midi(pitch: Pitch):
    """Zamienia obiekt Pitch (np. C#4) na numer nuty MIDI (np. 61)."""
    base = NOTE_OFFSETS.get(pitch.note_letter.lower(), 0)

    # Obliczamy numer: (oktawa + 1) * 12 + baza
    # W MIDI C4 to zazwyczaj 60 (czyli (4+1)*12 + 0)
    midi_note = (pitch.octave + 1) * 12 + base

    if pitch.accidental == 'sharp':
        midi_note += 1
    elif pitch.accidental == 'flat':
        midi_note -= 1

    return midi_note


# --- Klasy Zdarzeń IR (Intermediate Representation) ---
# To jest nasza "płaska" lista instrukcji dla generatora MIDI.

class IREvent:
    def __init__(self, time):
        self.time = int(time)  # Czas absolutny w tickach

    def __repr__(self):
        return f"Event(@{self.time})"


class NoteOnEvent(IREvent):
    def __init__(self, time, note_number, velocity=64):
        super().__init__(time)
        self.note_number = note_number
        self.velocity = velocity

    def __repr__(self):
        return f"NoteOn (@{self.time}, note={self.note_number}, vel={self.velocity})"


class NoteOffEvent(IREvent):
    def __init__(self, time, note_number, velocity=0):
        super().__init__(time)
        self.note_number = note_number
        self.velocity = velocity

    def __repr__(self):
        return f"NoteOff(@{self.time}, note={self.note_number})"


class ProgramChangeEvent(IREvent):
    """Zmiana instrumentu"""

    def __init__(self, time, program_number):
        super().__init__(time)
        self.program_number = program_number

    def __repr__(self):
        return f"ProgramChange(@{self.time}, prog={self.program_number})"


# --- Główny Generator ---

class IrGenerator:
    def __init__(self, context: CompilationContext):
        self.context = context

    def generate(self, ast: Tune):
        print(">>> Rozpoczynam generację Reprezentacji Pośredniej (IR)...")
        ir_tracks = []

        for track in ast.tracks:
            # Lista zdarzeń dla tej konkretnej ścieżki
            events = []
            current_time = 0  # Licznik czasu (w tickach)

            # Ustawienie instrumentu na początku (czas 0)
            if track.instrument:
                # Pobieramy numer instrumentu z mapy w semantic_analyzer
                prog_num = INSTRUMENT_MAP.get(track.instrument.name, 0)
                events.append(ProgramChangeEvent(0, prog_num))

            # Przetwarzanie komend
            for cmd in track.commands:
                # Oblicz czas trwania w tickach
                # duration.value to np. 1.5 (beata)
                # ticks_per_beat to np. 480
                duration_ticks = int(cmd.duration.value * self.context.ticks_per_beat)

                if isinstance(cmd, Note):
                    midi_note = pitch_to_midi(cmd.pitch)
                    # Włącz nutę TERAZ
                    events.append(NoteOnEvent(current_time, midi_note))
                    # Wyłącz nutę PÓŹNIEJ (teraz + czas trwania)
                    events.append(NoteOffEvent(current_time + duration_ticks, midi_note))

                    # Przesuń suwak czasu
                    current_time += duration_ticks

                elif isinstance(cmd, Chord):
                    # Akord: wszystkie nuty startują w tym samym czasie
                    midi_notes = [pitch_to_midi(p) for p in cmd.pitches]

                    for mn in midi_notes:
                        events.append(NoteOnEvent(current_time, mn))
                        events.append(NoteOffEvent(current_time + duration_ticks, mn))

                    # Czas przesuwa się tylko raz (o długość akordu)
                    current_time += duration_ticks

                elif isinstance(cmd, Rest):
                    # Pauza: po prostu przesuwamy czas, nie generujemy dźwięku
                    current_time += duration_ticks

            # Sortowanie zdarzeń
            events.sort(key=lambda x: x.time)

            ir_tracks.append({
                'name': track.name,
                'events': events
            })

        print(">>> Generacja IR zakończona sukcesem.")
        return ir_tracks