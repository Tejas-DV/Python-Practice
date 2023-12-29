import re
from collections import defaultdict

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return set(words)

def spell_check(file_path, dictionary):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)

    misspelled_words = defaultdict(list)
    for word in words:
        if word.lower() not in dictionary:
            misspelled_words[word.lower()].append(1)

    return misspelled_words

# testing the function
dictionary = load_dictionary("english_words.txt")
file_path = "sample.txt"
print("Misspelled words:", spell_check(file_path, dictionary))