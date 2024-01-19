def have_opposite_signs(x, y):
    return (x ^ y) < 0

# Usage
print(have_opposite_signs(42, -23)) # True
print(have_opposite_signs(0, 7)) # False