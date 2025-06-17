# braille_mapping.py

# Braille dots: D=1, W=2, Q=3, K=4, O=5, P=6
# Mapping English letters to QWERTY Braille key sets
braille_qwerty_map = {
    'a': {'D'},
    'b': {'D', 'W'},
    'c': {'D', 'K'},
    'd': {'D', 'K', 'O'},
    'e': {'D', 'O'},
    'f': {'D', 'W', 'K'},
    'g': {'D', 'W', 'K', 'O'},
    'h': {'D', 'W', 'O'},
    'i': {'W', 'K'},
    'j': {'W', 'K', 'O'},
    'k': {'D', 'Q'},
    'l': {'D', 'Q', 'W'},
    'm': {'D', 'Q', 'K'},
    'n': {'D', 'Q', 'K', 'O'},
    'o': {'D', 'Q', 'O'},
    'p': {'D', 'Q', 'W', 'K'},
    'q': {'D', 'Q', 'W', 'K', 'O'},
    'r': {'D', 'Q', 'W', 'O'},
    's': {'Q', 'W', 'K'},
    't': {'Q', 'W', 'K', 'O'},
    'u': {'D', 'Q', 'P'},
    'v': {'D', 'Q', 'W', 'P'},
    'w': {'W', 'K', 'O', 'P'},
    'x': {'D', 'Q', 'K', 'P'},
    'y': {'D', 'Q', 'K', 'O', 'P'},
    'z': {'D', 'Q', 'O', 'P'}
}
