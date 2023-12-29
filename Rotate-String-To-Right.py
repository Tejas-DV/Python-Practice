def rotate_array(input_array, rotation_count):
	rotation_count %= len(input_array)
	return input_array[-rotation_count:] + input_array[:-rotation_count]

# testing the function
input_array = ["book", "keeper", "an", "efficient", "program"]
rotation_count = 3
print("Input array:", input_array)
print("Array after rotation:", rotate_array(input_array, rotation_count))