def factorial(num):
    result = 1                  # Store the factorial result

    for i in range(1, num + 1): # Go from 1 to num
        result = result * i     # Multiply result by current number

    return result               # Return the factorial


num = 5                         # Example input

result = factorial(num)         # Call the function

print("Input number:", num)     # Print input
print("Factorial:", result)     # Print result


# Multiply all numbers from 1 to num.
# 5! = 1 × 2 × 3 × 4 × 5 = 120