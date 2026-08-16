"""
===========================================================
Problem 1: Check Whether a Number is Even or Odd
===========================================================

Example 1:

Input:
10

Expected Output:
Even


Example 2:

Input:
7

Expected Output:
Odd


Example 3:

Input:
0

Expected Output:
Even


Requirements:
- Take an integer as input.
- Check whether the number is even or odd.
- Use the modulo (%) operator.
"""


def check_even_odd(num):
    # Write your code here
    if num%2==0:
        return "Even"
    return "Odd"



num = 2
print("Input number:", num)
result = check_even_odd(num)
print("Result:", result)

