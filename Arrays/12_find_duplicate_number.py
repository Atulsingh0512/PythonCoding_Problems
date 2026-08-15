"""
===========================================================
Problem 12: Find the Duplicate Number
===========================================================

Example 1:

Input:
[1, 2, 3, 4, 2]

Expected Output:
2


Example 2:

Input:
[1, 3, 4, 2, 3]

Expected Output:
3


Example 3:

Input:
[5, 1, 2, 3, 4, 5]

Expected Output:
5

"""

def find_duplicate(arr):
    result = set()
    for num in arr:
        if num in result:
            return num
        result.add(num)
    return None

arr=[1, 5, 2, 3, 4, 5]
print("Array is",arr)
result=find_duplicate(arr)
print("result array",result)
#Logic: Store visited elements in a set; if an element is already present, it is the duplicate.