def reverse_bits(n):
    result = 0
    while n:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Usage
print(reverse_bits(42)) # 87