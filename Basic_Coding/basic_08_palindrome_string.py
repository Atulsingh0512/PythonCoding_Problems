"""
===========================================================
Problem 8: Check if a String is a Palindrome
===========================================================

Input Examples:

1. Input: "madam"
   Expected Output: Palindrome

2. Input: "hello"
   Expected Output: Not Palindrome

3. Input: "racecar"
   Expected Output: Palindrome

4. Input: "level"
   Expected Output: Palindrome
"""


def is_palindrome_string(text):
    left=0  # Start from the first character
    right=len(text)-1    # Start from the last character
    while left<right:    # Continue until the pointers meet
        if text[left]!=text[right]:   # Compare characters at both ends

            return "Not Palindrome"   # Different characters mean not palindrome
        left+=1                       # Move left pointer forward
        right-=1                      # Move right pointer backward
    return "Palindrome"



# Example Input
text = "madam"

# Function Call
result = is_palindrome_string(text)

# Output
print("Input string:", text)
print("Result:", result)