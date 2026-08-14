"""
Problem: Find the Largest Element in an Array

Given an array of integers, find the largest element.

Example:
Input:  [10, 25, 7, 45, 18]
Output: 45

Approach:
1. Assume the first element is the largest.
2. Traverse the array.
3. Compare each element with the current largest.
4. If the current element is greater, update largest.

Time Complexity: O(n)
Space Complexity: O(1)

Time Complexity:
O(n)

Why?
→ We traverse every element once.
→ There are n elements.
→ Therefore n operations → O(n)

Space Complexity:
O(1)

Why?
→ We only use a few variables.
→ We don't create extra storage proportional to n.
→ Therefore O(1)
"""


def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest


arr=[10,25,7,45,18]
result=find_largest(arr)
print("Input",arr)
print("Largest element",result)