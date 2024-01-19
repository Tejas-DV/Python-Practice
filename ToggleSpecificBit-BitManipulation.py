def toggle_bit(n, pos):
    mask = 1 << pos
    return n ^ mask

# Usage
print(toggle_bit(5, 1)) # 1
print(toggle_bit(8, 2)) # 8