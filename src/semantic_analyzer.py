from src.ast_nodes import *

# Mapa instrumentów MIDI (Standard General MIDI)
# https://en.wikipedia.org/wiki/General_MIDI
INSTRUMENT_MAP = {
    'piano': 0, 'bright_piano': 1, 'electric_piano': 2, 'honky_tonk': 3,
    'guitar': 24, 'acoustic_guitar': 24, 'electric_guitar': 27, 'bass': 32,
    'violin': 40, 'strings': 48, 'trumpet': 56, 'sax': 65, 'flute': 73,
    'drums': 118,
    'kazoo': 56,
}


class CompilationContext:
    """
    Obiekt przechowujący wynik analizy semantycznej.
    """

    def __init__(self):
        self.tempo = 120  # Domyślne tempo
        self.ticks_per_beat = 480  # Domyślna rozdzielczość
        self.time_signature = (4, 4)  # Domyślne metrum
        self.errors = []  # Lista znalezionych błędów


class SemanticAnalyzer:
    def analyze(self, ast: Tune):
        context = CompilationContext()

        print(">>> Rozpoczynam analizę semantyczną...")

        # Analiza ustawień globalnych
        self._analyze_globals(ast.global_settings, context)

        # Analiza ścieżek
        self._analyze_tracks(ast.tracks, context)

        # Raportowanie błędów
        if context.errors:
            error_msg = "\n".join(context.errors)
            print("\n!!! Znaleziono błędy semantyczne !!!")
            print(error_msg)
            # Rzucamy wyjątek z treścią błędów dla GUI/CLI
            raise Exception(f"Błędy walidacji:\n{error_msg}")

        print(">>> Analiza semantyczna zakończona sukcesem.")
        return context

    def _analyze_globals(self, settings, context):
        defined_tempo = False
        defined_ticks = False
        defined_time = False

        for setting in settings:
            if isinstance(setting, GlobalSetting):
                if setting.key == 'tempo':
                    if defined_tempo:
                        context.errors.append(
                            f"[Linia {setting.line}] Błąd: Tempo zostało zdefiniowane więcej niż raz.")
                    if setting.value <= 0:
                        context.errors.append(
                            f"[Linia {setting.line}] Błąd: Tempo musi być dodatnie, znaleziono: {setting.value}")
                    context.tempo = int(setting.value)
                    defined_tempo = True

                elif setting.key == 'ticks':
                    if defined_ticks:
                        context.errors.append(
                            f"[Linia {setting.line}] Błąd: Ticks (rozdzielczość) zdefiniowane więcej niż raz.")
                    if setting.value <= 0:
                        context.errors.append(f"[Linia {setting.line}] Błąd: Ticks musi być dodatnie.")
                    context.ticks_per_beat = int(setting.value)
                    defined_ticks = True

            elif isinstance(setting, TimeSignatureSetting):
                if defined_time:
                    context.errors.append(f"[Linia {setting.line}] Błąd: Metrum zdefiniowane więcej niż raz.")

                if setting.numerator <= 0 or setting.denominator <= 0:
                    context.errors.append(
                        f"[Linia {setting.line}] Błąd: Licznik i mianownik metrum muszą być dodatnie.")

                # Sprawdzenie czy mianownik jest potęgą dwójki
                if not (setting.denominator & (setting.denominator - 1) == 0) and setting.denominator != 0:
                    context.errors.append(
                        f"[Linia {setting.line}] Ostrzeżenie: Mianownik metrum {setting.denominator} jest nietypowy (standardowo potęga 2: 4, 8, 16).")

                context.time_signature = (setting.numerator, setting.denominator)
                defined_time = True

    def _analyze_tracks(self, tracks, context):
        if not tracks:
            context.errors.append("Błąd: Utwór nie zawiera żadnych ścieżek (tracks).")
            return

        # Sprawdzamy unikalność nazw ścieżek
        track_names = set()

        for track in tracks:
            # Walidacja nazwy ścieżki
            if track.name in track_names:
                context.errors.append(f"[Linia {track.line}] Błąd: Zduplikowana nazwa ścieżki: '{track.name}'")
            track_names.add(track.name)

            # Walidacja instrumentu
            if track.instrument:
                inst_name = track.instrument.name
                if inst_name not in INSTRUMENT_MAP:
                    context.errors.append(
                        f"[Linia {track.instrument.line}] Błąd: Nieznany instrument '{inst_name}' w ścieżce '{track.name}'. Dostępne: {list(INSTRUMENT_MAP.keys())}")

            # Walidacja komend
            self._analyze_commands(track.commands, context, track.name)

    def _analyze_commands(self, commands, context, track_name):
        for cmd in commands:
            if isinstance(cmd, Note):
                self._validate_pitch(cmd.pitch, context, track_name)
            elif isinstance(cmd, Chord):
                for pitch in cmd.pitches:
                    self._validate_pitch(pitch, context, track_name)

    def _validate_pitch(self, pitch, context, track_name):
        # MIDI obsługuje nuty od 0 do 127.
        if pitch.octave < -1 or pitch.octave > 9:
            context.errors.append(
                f"[Linia {pitch.line}] Błąd w ścieżce '{track_name}': Oktawa {pitch.octave} jest poza zakresem MIDI (-1 do 9).")