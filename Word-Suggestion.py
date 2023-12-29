def load_dictionary(file_path):
    	with open(file_path, 'r') as file:
         words = file.read().splitlines()
         return set(words)

def autocomplete(prefix, dictionary):
    return [word for word in dictionary if word.startswith(prefix)]

# testing the function
dictionary = load_dictionary("english_words.txt")
print("Suggested words:", autocomplete("hel", dictionary))