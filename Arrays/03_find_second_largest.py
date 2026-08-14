"""
===========================================================
Problem 3: Find the Second Largest Element
===========================================================

Problem:
Given an array of integers, find the SECOND LARGEST
DISTINCT element in the array.

-----------------------------------------------------------
Example 1
-----------------------------------------------------------

Input:
[10, 25, 7, 45, 18]

Expected Output:
25

"""



def second_largest(arr):
   if len(set(arr)) <2:
      return None
   largest=float("-inf") # -infinite
   second_largest=float("-inf") # -infinite
   for num in arr:
              # Found a new largest element

      if num >largest:
         second_largest=largest
         largest=num

        # num is between largest and second largest

      elif num >second_largest and num !=largest:
         second_largest=num
   return second_largest



arr=[10,25,7,45,18]
result=second_largest(arr)
print("Elements are:", arr)
print("Second Largest is :", result)