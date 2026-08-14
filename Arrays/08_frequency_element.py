"""
===========================================================
Problem 8: Find Frequency of an Element
===========================================================

Example 1:

Input:
Array = [10, 20, 10, 30, 10, 40]
Target = 10

Expected Output:
Frequency: 3


Example 2:

Input:
Array = [5, 2, 5, 8, 5, 2]
Target = 2

Expected Output:
Frequency: 2


Example 3:

Input:
Array = [1, 2, 3, 4, 5]
Target = 10

Expected Output:
Frequency: 0


Requirements:
- Count how many times the target appears in the array.
- Use a loop.
- Do not use count().
"""


def find_frequency(arr, target):
    # Write your code here
    count=0
    for num in arr:
        if num==target:
            count+=1
    return count




arr = [10, 20, 10, 30, 10, 40]
target = 10
print("Input array:", arr)
print("Target:", target)


result = find_frequency(arr, target)


print("Frequency:", result)