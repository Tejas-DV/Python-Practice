def swap_bits(n, pos1, pos2):
    mask1 = 1 << pos1
    mask2 = 1 << pos2
    if n & mask1:
        n |= mask2
    else:
        n &= ~mask2
    if n & mask2:
        n |= mask1
    else:
        n &= ~mask1
    return n

# Usage
print(swap_bits(7, 1, 2)) # 7
print(swap_bits(29, 1, 3)) # 19