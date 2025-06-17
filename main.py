# main.py

import itertools
from braille_mapping import braille_qwerty_map
from Levenshtein import distance as levenshtein

# Load dictionary
def load_words(file_path):
    with open(file_path, 'r') as f:
        return [word.strip() for word in f.readlines()]

# Convert a word to its QWERTY braille pattern
def word_to_qwerty_braille(word):
    return [sorted(braille_qwerty_map.get(char, [])) for char in word]

# Suggest closest words
def suggest_words(user_input, word_list):
    suggestions = []
    for word in word_list:
        pattern = word_to_qwerty_braille(word)
        dist = levenshtein(str(user_input), str(pattern))
        suggestions.append((word, dist))
    return sorted(suggestions, key=lambda x: x[1])[:5]

def get_user_input():
    print("Enter Braille letters using sets of keys (D, W, Q, K, O, P).")
    print("Example: For 'C', enter: D,K")
    input_seq = []
    while True:
        keys = input("Enter Braille letter (comma-separated, or 'done' to finish): ").strip()
        if keys.lower() == 'done':
            break
        input_seq.append(sorted(keys.upper().split(',')))
    return input_seq

if __name__ == "__main__":
    dictionary = load_words("dictionary.txt")
    user_braille_input = get_user_input()
    suggestions = suggest_words(user_braille_input, dictionary)

    print("\nTop Suggestions:")
    for word, score in suggestions:
        print(f"{word} (score: {score})")
