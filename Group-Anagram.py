def group_anagrams(words):
    # Create a dictionary to store the grouped anagrams
    anagram_groups = {}

    # Iterate over each word in the list
    for word in words:
        # Sort the characters in the word alphabetically
        sorted_word = ''.join(sorted(word))

        # If the sorted word is already in the dictionary, append the original word to the value list
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        # Otherwise, add a new entry to the dictionary with the sorted word as the key and a list containing the original word as the value
        else:
            anagram_groups[sorted_word] = [word]

    # Return the dictionary of grouped anagrams
    return anagram_groups

# Example usage:

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
grouped_anagrams = group_anagrams(words)
for key, value in grouped_anagrams.items():
    print(key, value)