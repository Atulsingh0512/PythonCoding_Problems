"""
===========================================================
Problem 7: Calculate Sum and Average of an Array
===========================================================

Example 1:

Input:
[10, 20, 30, 40, 50]

Expected Output:
Sum: 150
Average: 30.0


Example 2:

Input:
[5, 10, 15]

Expected Output:
Sum: 30
Average: 10.0


Requirements:
- Calculate the sum of all elements.
- Calculate the average of the elements.
- Use a loop to calculate the sum.
- Do not use sum().
"""


def calculate_sum_average(arr):
    # Write your code here
    sum=0
    avg=0
    for num in arr:
        sum+=num
        avg=sum/len(arr)
    return sum,avg


arr = [10, 20, 30, 40, 50]

total, average = calculate_sum_average(arr)

print("Input array:", arr)
print("Sum:", total)
print("Average:", average)