def calculate_load_factor(hash_table):
    num_keys = len(hash_table)
    capacity = len(hash_table[0])
    load_factor = (num_keys / capacity)
    return load_factor