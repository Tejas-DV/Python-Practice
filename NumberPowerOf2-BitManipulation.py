def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Usage
print(is_power_of_two(8)) # True
print(is_power_of_two(9)) # False