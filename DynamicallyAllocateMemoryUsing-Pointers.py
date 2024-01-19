import ctypes

def create_array(size):
    array_type = ctypes.c_int * size
    return array_type()

# Usage
arr = create_array(5)
for i in range(5):
    arr[i] = i + 1
print(arr[:]) # [1, 2, 3, 4, 5]