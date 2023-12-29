def is_palindrome(string):
    return string == string[::-1]

def partition(input_string):
    partition_list = []
    for i in range(1, len(input_string)+1):
        prefix = input_string[:i]
        if is_palindrome(prefix):
            suffix = input_string[i:]
            for j in range(len(suffix), -1, -1):
                if is_palindrome(suffix[:j]):
                    partition_list.append(prefix + ',' + suffix[:j])
                    if j < len(suffix):
                        partition_list.append(prefix + ',' + suffix[:j] + ',' + suffix[j:])
    return partition_list

# testing the function
input_string = "racecar"
print("All possible palindromic partitions of the input string:", partition(input_string))