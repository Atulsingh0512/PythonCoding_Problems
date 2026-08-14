"""
===========================================================
Problem 5: Check if an Array is Sorted
===========================================================

Example 1:

Input:
[1, 2, 3, 4, 5]

Expected Output:
True


Example 2:

Input:
[1, 3, 2, 4, 5]

Expected Output:
False


Example 3:

Input:
[10, 20, 30, 40]

Expected Output:
True


Example 4:

Input:
[5, 4, 3, 2, 1]

Expected Output:
False

"""

def is_sorted(arr):
    # Write your code here
    for i in range (len(arr)-1):
        if arr[i] >arr[i+1]:
            return False
    return True



arr = [1, 6, 3, 4, 5]
print("Input array:", arr)
result = is_sorted(arr)
print("Is array sorted?", result)

"""Logic:

- Compare each element with the next element.
- If arr[i] > arr[i + 1], the array is not sorted.
- Immediately return False.
- If no such pair is found, return True.

Time Complexity: O(n)
Space Complexity: O(1)
Pattern: Array Traversal
"""