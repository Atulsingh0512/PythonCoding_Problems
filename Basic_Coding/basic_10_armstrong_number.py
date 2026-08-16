"""
===========================================================
Problem 10: Check Armstrong Number
===========================================================

An Armstrong number is a number where the sum of each digit
raised to the power of the total number of digits is equal
to the original number.

Input Examples:

1. Input: 153
   Expected Output: Armstrong

2. Input: 123
   Expected Output: Not Armstrong

3. Input: 370
   Expected Output: Armstrong

4. Input: 9474
   Expected Output: Armstrong
"""


def is_armstrong(num):
    original = num                 # Store the original number
    digits = 0                     # Store the total number of digits
    temp = num                     # Create a temporary number for counting digits

    while temp > 0:                # Continue until all digits are processed
        digits += 1                # Increase digit count by 1
        temp = temp // 10           # Remove the last digit

    total = 0                      # Store the sum of powered digits
    temp = num                     # Reset temp to the original number

    while temp > 0:                # Process each digit again
        digit = temp % 10           # Get the last digit
        total += digit ** digits    # Add digit raised to the number of digits
        temp = temp // 10            # Remove the last digit

    if total == original:            # Compare calculated sum with original number
        return "Armstrong"           # Number is an Armstrong number

    return "Not Armstrong"           # Number is not an Armstrong number


num = 153                            # Example input

result = is_armstrong(num)           # Call the function

print("Input number:", num)          # Print the input number
print("Result:", result)             # Print the result