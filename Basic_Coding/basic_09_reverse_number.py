"""
===========================================================
Problem 9: Reverse a Number
===========================================================

Input Examples:

1. Input: 12345
   Expected Output: 54321

2. Input: 9876
   Expected Output: 6789

3. Input: 1000
   Expected Output: 1

4. Input: 121
   Expected Output: 121
"""


def reverse_number(num):
    reverse=0
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse


# Example Input
num = 56745

# Function Call
result = reverse_number(num)

# Output
print("Input number:", num)
print("Reversed number:", result)