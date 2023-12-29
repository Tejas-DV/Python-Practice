import re
from collections import defaultdict
import textwrap

def word_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
	
    words = re.findall(r'\b\w+\b', textwrap)
    word_counts = defaultdict(int)

    for word in words:
	    word_counts[word.lower()] += 1 
	
    return word_counts

# testing the function
file_path = "sample.txt"
print("Word count results:", word_count(file_path))