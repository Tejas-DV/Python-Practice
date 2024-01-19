def reverse_array(arr):
    # Calculate the length of the array
    length = len(arr)

    # Reverse the array using slicing
    arr[:] = arr[::-1]

# Test the function
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr) # [5, 4, 3, 2, 1]