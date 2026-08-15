"""
===========================================================
Problem 10: Move All Zeroes to the End
===========================================================

Example 1:

Input:
[0, 1, 0, 3, 12]

Expected Output:
[1, 3, 12, 0, 0]


Example 2:

Input:
[1, 0, 2, 0, 3]

Expected Output:
[1, 2, 3, 0, 0]


Example 3:

Input:
[1, 2, 3, 4]

Expected Output:
[1, 2, 3, 4]

"""


def move_zeroes(arr):
    # Write your code here
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos],arr[i]=arr[i],arr[pos]
            pos+=1
    return arr



arr = [0, 1, 0, 3, 12]
result = move_zeroes(arr)
print("Input array:", [0, 1, 0, 3, 12])
print("After moving zeroes:", result)

# Find a non-zero number → put it at pos → move pos forward.