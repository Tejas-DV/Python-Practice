def find_most_frequent(nums):
    hash_table = {}
    for num in nums:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1
    max_freq = max(hash_table.values())
    most_frequent = [k for k, v in hash_table.items() if v == max_freq]
    return most_frequent