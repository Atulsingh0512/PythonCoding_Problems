"""
===========================================================
Problem 11: Find the Missing Number
===========================================================

The array contains numbers from 1 to n.
Exactly one number is missing.

Example 1:

Input:
[1, 2, 3, 5]

Expected Output:
4


Example 2:

Input:
[1, 2, 4, 5, 6]

Expected Output:
3


Example 3:

Input:
[1, 3, 4, 5]

Expected Output:
2

"""
res=0
def missing_number(arr):
    n=len(arr)+1
    expected_sum=n*(n+1)//2
    actual_sum=0

    for num in arr:
        actual_sum=actual_sum+num
    return expected_sum-actual_sum


arr=[1,2,4,5,6]
print("Array is",arr)
result=missing_number(arr)
print("result array",result)