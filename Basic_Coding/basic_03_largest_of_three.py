def find_largest(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c


# Example Input
a = 10
b = 25
c = 15

# Function Call
result = find_largest(a, b, c)

# Output
print("Input numbers:", a, b, c)
print("Largest number:", result)


# Expected Output:
# Input numbers: 10 25 15
# Largest number: 25