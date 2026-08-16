"""
===========================================================
Problem 7: Palindrome Number
===========================================================

Input Examples:

1. Input: 121
   Expected Output: Palindrome

2. Input: 123
   Expected Output: Not Palindrome

3. Input: 1221
   Expected Output: Palindrome

4. Input: 12321
   Expected Output: Palindrome
"""

# Logic: Reverse the number digit by digit and compare the reversed number with the original number.
def is_palindrome(num):
    original=num
    reverse=0
    while num>0:                                        # Continue until all digits are processed
        digit=num%10                                    # Get the last digit
        reverse=reverse*10+digit                        # Add the digit to the reversed number
        num=num//10                                     # Remove the last digit
    if original==reverse:
        return "Palindrome"
    return "Not Palindrome"


# Example Input
num = 123

# Function Call
result = is_palindrome(num)

# Output
print("Input number:", num)
print("Result:", result)