from itertools import permutations

def find_permutations(input_string):
    permutation_list = [''.join(p) for p in permutations(input_string)]
    return sorted(set(permutation_list))  
        # remove duplicates and sort the list.

# testing the function
input_string = "abc"
print("All permutations of the input string:", find_permutations(input_string))