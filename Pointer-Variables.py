import ctypes

# Declare a pointer to an integer
ptr_int = ctypes.POINTER(ctypes.c_int)

# Initialize the pointer with the address of an integer variable
value_int = ctypes.c_int(10)
ptr_int = ctypes.pointer(value_int)

# Print the type and value of the pointer
print(f"Type: {ptr_int}, Value: {ptr_int.contents.value}")
