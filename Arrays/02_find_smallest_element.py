"""===========================================================
Problem 2: Find the Smallest Element
===========================================================

Problem:
Given an array of integers, find the smallest element
in the array.

Example 1:
Input:
[10, 25, 7, 45, 18]

Expected Output:
7


Example 2:
Input:
[34, 12, 89, 5, 23]

Expected Output:
5
"""



def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

    
arr=[10, 25, 7, 45, 18]
result = find_smallest(arr)
print("Input array:", arr)
print("Smallest element in the array:", result)


# ===========================================================
# Time & Space Complexity
# ===========================================================

"""
Time Complexity: O(n)

Explanation:
- Let n = number of elements in the array.
- The for loop visits every element in the array once.
- Therefore, if the array has n elements, the loop runs n times.
- Each comparison takes constant time O(1).
- Total work = n × O(1) = O(n).

Therefore:
Time Complexity = O(n)


Space Complexity: O(1)

Explanation:
- We only use one extra variable: smallest.
- The variable num is also used during the loop.
- We are not creating another array or data structure.
- The amount of extra memory does not increase when n increases.

Therefore:
Space Complexity = O(1).
"""