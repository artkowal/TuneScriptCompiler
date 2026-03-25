import sys
import os
from antlr4 import *

# Ścieżki
sys.path.append('./generated')
sys.path.append('./src')

# Importy
from generated.grammar.TuneScriptLexer import TuneScriptLexer
from generated.grammar.TuneScriptParser import TuneScriptParser
from src.ast_builder import AstBuilder
from src.semantic_analyzer import SemanticAnalyzer
from src.ir_generator import IrGenerator
from src.midi_generator import MidiGenerator


def main():
    # Konfiguracja plików
    input_file = 'examples/kotek.tune'

    output_filename = os.path.basename(input_file).replace('.tune', '.mid')
    output_file = os.path.join('output', output_filename)

    print(f"--- [START] Kompilacja: {input_file} -> {output_file} ---")

    # 1. Front-end
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = TuneScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TuneScriptParser(stream)
    cst = parser.tune()

    # 2. AST
    ast_builder = AstBuilder()
    ast = ast_builder.visit(cst)

    # 3. Analiza Semantyczna
    analyzer = SemanticAnalyzer()
    try:
        context = analyzer.analyze(ast)
    except Exception as e:
        print(f"\n[BŁĄD] {e}")
        return

        # 4. Generacja IR
    ir_gen = IrGenerator(context)
    ir_data = ir_gen.generate(ast)


    print("\n--- Generacja pliku MIDI ---")

    midi_gen = MidiGenerator(context)
    midi_file = midi_gen.generate(ir_data)

    # Zapis do pliku we wskazanym folderze
    try:
        midi_file.save(output_file)
        print(f"\n[SUKCES] Utworzono plik: {output_file}")
        print("Możesz go teraz otworzyć w dowolnym odtwarzaczu MIDI!")
    except FileNotFoundError:
        print(f"\n[BŁĄD] Nie znaleziono folderu 'output'. Upewnij się, że folder 'output' istnieje w projekcie.")


if __name__ == '__main__':
    main()