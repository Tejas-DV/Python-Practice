def swap_values(a, b):
    # Swap the values of the variables using a temporary variable
    temp = a
    a = b
    b = temp

# Test the function
x = 5
y = 10
swap_values(x, y)
print("x =", x) # x = 10
print("y =", y) # y = 5