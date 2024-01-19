def str_concat(s1, s2):
    result = ''
    for char in s1:
        result += char
    for char in s2:
        result += char
    return result

# Usage
print(str_concat("hello", " world")) # "hello world"