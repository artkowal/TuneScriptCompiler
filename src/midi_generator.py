import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
from src.ir_generator import NoteOnEvent, NoteOffEvent, ProgramChangeEvent


class MidiGenerator:
    def __init__(self, context):
        self.context = context

    def generate(self, ir_tracks):
        print(">>> Rozpoczynam generację pliku binarnego MIDI...")

        # Tworzymy obiekt MidiFile
        # type=1 oznacza plik wielościeżkowy (multitrack)
        mid = MidiFile(type=1, ticks_per_beat=self.context.ticks_per_beat)

        for ir_track_data in ir_tracks:
            # Tworzymy nową ścieżkę MIDI
            midi_track = MidiTrack()
            mid.tracks.append(midi_track)

            # 1. Metadane ścieżki (Nazwa, Tempo, Metrum)
            # Ustaw nazwę ścieżki
            midi_track.append(MetaMessage('track_name', name=ir_track_data['name'], time=0))

            # Ustaw tempo
            tempo_microseconds = mido.bpm2tempo(self.context.tempo)
            midi_track.append(MetaMessage('set_tempo', tempo=tempo_microseconds, time=0))

            # Ustaw Metrum (Time Signature)
            num, den = self.context.time_signature
            midi_track.append(MetaMessage('time_signature', numerator=num, denominator=den, time=0))

            # 2. Konwersja zdarzeń IR na komunikaty MIDI
            # MIDI używa "delta-time" (czas od poprzedniego zdarzenia)

            last_event_time = 0

            for event in ir_track_data['events']:
                # Oblicz delta-time
                delta_time = event.time - last_event_time

                # Zabezpieczenie
                if delta_time < 0:
                    delta_time = 0

                # Generuj odpowiedni komunikat mido
                if isinstance(event, NoteOnEvent):
                    msg = Message('note_on', note=event.note_number, velocity=event.velocity, time=delta_time)
                    midi_track.append(msg)

                elif isinstance(event, NoteOffEvent):
                    msg = Message('note_off', note=event.note_number, velocity=event.velocity, time=delta_time)
                    midi_track.append(msg)

                elif isinstance(event, ProgramChangeEvent):
                    msg = Message('program_change', program=event.program_number, time=delta_time)
                    midi_track.append(msg)

                # Zaktualizuj czas ostatniego zdarzenia
                last_event_time = event.time

        print(">>> Generacja MIDI zakończona sukcesem.")
        return mid