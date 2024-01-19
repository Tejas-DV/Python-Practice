def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    hash_table = {}
    for char in str1:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    for char in str2:
        if char in hash_table:
            hash_table[char] -= 1
        else:
            return False
    for key in hash_table:
        if hash_table[key] != 0:
            return False
    return True