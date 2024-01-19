def str_copy_pointer(s):
    result = ''
    for char in s:
        result += char
    return result

# Usage
ptr = str_copy_pointer("hello")
print(ptr) # "hello"