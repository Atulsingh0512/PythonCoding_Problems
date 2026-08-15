"""
===========================================================
Problem 9: Remove Duplicates from a Sorted Array
===========================================================

Example 1:

Input:
[1, 1, 2, 2, 3, 4, 4, 5]

Expected Output:
[1, 2, 3, 4, 5]


Example 2:

Input:
[1, 1, 1, 2, 2, 3]

Expected Output:
[1, 2, 3]


Example 3:

Input:
[1, 2, 3, 4, 5]

Expected Output:
[1, 2, 3, 4, 5]


"""


def remove_duplicates(arr):
    # Write your code here
    if len(arr)==0:
        return []
    result=[arr[0]]
    for i in range (1,len(arr)):
        if arr[i]!=arr[i-1]:
            result.append(arr[i])
    return result


arr = [1, 1, 2, 2, 3, 4, 4, 5]
print("Input array:", arr)
result = remove_duplicates(arr)
print("Array after removing duplicates:", result)