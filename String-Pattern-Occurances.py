import re

def find_pattern(input_string, pattern):
    return [match.span() for match in re.finditer(pattern, input_string)]

# testing the function
input_string = "Hello, there! Welcome to this program."
pattern = "this program"
print("All occurrences of the pattern in the input string:", find_pattern(input_string, pattern))