// 2 podejscia ANTLER do generowania MIDI
// Jakie ?? Sprawdzić
grammar TuneScript;

// Reguła startowa (S)
tune: globalSettings trackList EOF;

// Ustawienia Globalne (G, T)
globalSettings: globalSetting* ; // G -> T G | ε

globalSetting
    : TEMPO EQ NUMBER       // T -> tempo = number
    | TICKS EQ NUMBER       // T -> ticks = number
    | TIME EQ timeSignature // T -> time = 3/4
    ;

timeSignature
    : NUMBER '/' NUMBER
    ;

// Ścieżki (K, I)
trackList: trackDefinition+ ; // K -> I K | I

trackDefinition
    : TRACK STRING LBRACE trackBody RBRACE // I -> track "id" { B }
    ;

// Blok Ścieżki (B, J, C)
trackBody: instrumentSetting? commandList ; // B -> J C

instrumentSetting
    : INSTRUMENT EQ ID  // J -> instrument = id | ε
    ;

commandList: command+ ; // C -> E C | E

// Instrukcje (E, N, A, R)
command
    : note   // E -> N
    | chord  // E -> A
    | rest   // E -> R
    ;

// Definicje Instrukcji (N, A, R)
note: PLAY pitch duration ; // N -> play H D

chord: PLAY L_ANGLE pitchList R_ANGLE duration ; // A -> play < L > D

rest: REST duration ; // R -> rest D

// Elementy Budulcowe (D, L, H, Y, Z)
duration
    : FOR NUMBER (BEAT | BEATS) // D -> for number beat | for number beats
    ;

pitchList
    : pitch+  // L -> H L | H
    ;

pitch
    : pitchName NUMBER // H -> P number
    ;

pitchName
    : NOTE_LETTER (SHARP | FLAT)? // P -> Y Z | Y
    ;

/* --- REGUŁY LEKSERA --- */

// Słowa kluczowe
TEMPO: 'tempo';
TICKS: 'ticks';
TIME: 'time';
TRACK: 'track';
INSTRUMENT: 'instrument';
PLAY: 'play';
REST: 'rest';
FOR: 'for';
BEAT: 'beat';
BEATS: 'beats';
SHARP: 'sharp';
FLAT: 'flat';

// Litery nut
NOTE_LETTER: 'c' | 'd' | 'e' | 'f' | 'g' | 'a' | 'b' ;

// Operatory i Separatory
EQ: '=';
LBRACE: '{';
RBRACE: '}';
L_ANGLE: '<';
R_ANGLE: '>';

// Typy danych
ID: [a-zA-Z_]+;
NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["])* '"';

// Ignorowane
WS: [ \t\r\n]+ -> skip; // Ignoruj białe znaki
LINE_COMMENT: '//' .*? '\n' -> skip; // komentarze