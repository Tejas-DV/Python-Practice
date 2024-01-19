def hash_table_insert(hash_table, key, value):
    index = hash_function(key)
    if hash_table[index] == None:
        hash_table[index] = key
        hash_table[index + 1] = value
    else:
        # handle collisions
        while hash_table[index] != None:
            index += 1
        hash_table[index] = key
        hash_table[index + 1] = value