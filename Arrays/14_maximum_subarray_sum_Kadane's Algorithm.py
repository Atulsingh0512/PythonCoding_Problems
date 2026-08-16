"""
===========================================================
Problem 14: Maximum Subarray Sum
===========================================================

Find the contiguous subarray with the largest sum.

Example 1:

Input:
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Expected Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the maximum sum.


Example 2:

Input:
[5, 4, -1, 7, 8]

Expected Output:
23

Explanation:
The entire array has the maximum sum.


Example 3:

Input:
[-5, -2, -8, -1]

Expected Output:
-1


Requirements:
- Find the maximum sum of a contiguous subarray.
- The subarray must contain at least one element.
- Try to solve it in O(n) time.
- Do not use nested loops.
"""
# The main idea of Kadane's Algorithm is:
# At every element, decide whether it is better to continue the current subarray 
# or start a new subarray from the current element.


def max_subarray_sum(arr):
    # Write your code here
    current_sum=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        current_sum=max(arr[i],current_sum+arr[i])
        max_sum=max(max_sum,current_sum)
    return max_sum

# Example Input
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Call the function
result = max_subarray_sum(arr)

# Output
print("Input array:", arr)
print("Maximum subarray sum:", result)