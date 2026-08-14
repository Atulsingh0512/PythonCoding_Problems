"""
===========================================================
Problem 4: Reverse an Array
===========================================================

Example 1:

Input:
[10, 25, 7, 45, 18]

Expected Output:
[18, 45, 7, 25, 10]


Example 2:

Input:
[1, 2, 3, 4, 5]

Expected Output:
[5, 4, 3, 2, 1]


Requirements:
- Write a function to reverse the array.
- Do not use reverse().
- Do not use slicing [::-1].
- Try to solve it using a loop.
"""


#TWO-POINTER TECHNIQUE

def reverse_array(arr):
    # Write your code here
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr


arr = [10, 25, 7, 45, 18]

print("Input array:", arr)
result = reverse_array(arr)
print("Reversed array:", result)


"""
Logic:
- Use two pointers: left at the beginning and right at the end.
- Swap the elements at left and right.
- Move left one step forward.
- Move right one step backward.
- Repeat until left >= right.
- This reverses the array in-place.

Time Complexity: O(n)
Space Complexity: O(1)
Pattern: Two Pointers
"""