def hash_table_contains(hash_table, key):
    index = hash_function(key)
    while hash_table[index] != None:
        if hash_table[index] == key:
            return True
        index += 1
    return False