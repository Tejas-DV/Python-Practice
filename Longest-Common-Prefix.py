def longest_common_prefix(array):
    # check if array is empty
    if len(array) == 0:
        return ""

    # sort the array
    array.sort()

    # compare the first and last strings
    first = array[0]
    last = array[-1]

    # find the longest common prefix
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

# testing the function
input_array = ["flower", "flow", "flight"]
print("Input array:", input_array)

lcp = longest_common_prefix(input_array)
print("Longest common prefix:", lcp)