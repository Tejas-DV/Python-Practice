def remove_duplicates(input_string):
    result = ""
    char_count = [0] * 26

    for char in input_string:
        char_index = ord(char) - ord('a')
        if char_count[char_index] == 0:
            result += char
            char_count[char_index] += 1

    return result

# testing the function
input_string = "boookkeeper"
print("Input string:", input_string)
print("String after removing duplicates:", remove_duplicates(input_string))

