"""===========================================================
Problem 13: Two Sum
===========================================================

Example 1:

Input:
Array = [2, 7, 11, 15]
Target = 9

Expected Output:
[0, 1]


Example 2:

Input:
Array = [3, 2, 4]
Target = 6

Expected Output:
[1, 2]


Example 3:

Input:
Array = [3, 3]
Target = 6

Expected Output:
[0, 1]


Requirements:
- Find two elements whose sum equals the target.
- Return their indices.
- Assume exactly one valid pair exists.
"""

# Logic: Store each number and its index in a dictionary; for each number, check whether target - number has already been seen.

def two_sum(arr,target):
    seen={}
    for i in range(len(arr)):
        complement=target-arr[i]
        if complement in seen:
            return [seen[complement],i]
        seen[arr[i]]=i
    return[]

arr = [3, 3]
target=6
print("original array is ",arr)
result=two_sum(arr,target)
print("Result index are",result)

