def str_equals(s1, s2):
    while s1 and s2:
        if s1[0] != s2[0]:
            return False
        s1 = s1[1:]
        s2 = s2[1:]
    return not s1 and not s2

# Usage
print(str_equals("hello", "hello")) # True
print(str_equals("hello", "world")) # False