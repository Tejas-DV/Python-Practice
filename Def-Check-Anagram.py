def check_anagram(string1, string2):
    # check if lengths are the same
    if len(string1) != len(string2):
        return False

    # create character count arrays
    count1 = [0] * 26
    count2 = [0] * 26

    # count characters in both strings
    for char in string1:
        count1[ord(char) - ord('a')] += 1
    for char in string2:
        count2[ord(char) - ord('a')] += 1

    # compare character count arrays
    for i in range(26):
        if count1[i] != count2[i]:
            return False

    return True

# testing the function
input_string1 = "listen"
input_string2 = "silent"
print("Input string 1:", input_string1)
print("Input string 2:", input_string2)

is_anagram = check_anagram(input_string1, input_string2)
print("Are they anagrams?", is_anagram)