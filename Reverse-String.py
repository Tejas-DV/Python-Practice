def reverse_array(array):
    # check if array is empty
    if len(array) == 0:
        return array

    # create a new array with reversed order
    reversed_array = array[::-1]

    return reversed_array

# testing the function
input_array = ["hello", "world", "how", "are", "you"]
print("Input array:", input_array)

reversed_array = reverse_array(input_array)
print("Reversed array:", reversed_array)