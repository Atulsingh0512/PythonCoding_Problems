"""
===========================================================
Problem 6: Count Even and Odd Numbers
===========================================================

Example 1:

Input:
[10, 25, 7, 45, 18, 20]

Expected Output:
Even numbers: 3
Odd numbers: 3


Example 2:

Input:
[1, 2, 3, 4, 5]

Expected Output:
Even numbers: 2
Odd numbers: 3


Requirements:
- Count how many even numbers are present.
- Count how many odd numbers are present.
- Use a loop.
"""


def count_even_odd(arr):
    # Write your code here
    even_count=0
    odd_count=0
    for num in arr:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count


arr = [10, 2, 7, 45, 18, 20]
even_count, odd_count = count_even_odd(arr)
print("Input array:", arr)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)