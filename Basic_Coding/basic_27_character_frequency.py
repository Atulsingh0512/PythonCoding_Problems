def digit_frequency(num):
    frequency = {}                    # Store digit and its frequency

    while num > 0:                    # Process every digit
        digit = num % 10              # Get the last digit

        if digit in frequency:
            frequency[digit] += 1     # Increase existing digit count
        else:
            frequency[digit] = 1      # Add digit for the first time

        num = num // 10                # Remove the last digit

    return frequency                  # Return frequency dictionary


num = 112233                           # Example input

result = digit_frequency(num)          # Call the function

print("Input number:", num)
print("Digit frequency:", result)

"""
Input number: 112233
Digit frequency: {3: 2, 2: 2, 1: 2}


num = 112233

digit = 3 → {3: 1}
digit = 3 → {3: 2}

digit = 2 → {3: 2, 2: 1}
digit = 2 → {3: 2, 2: 2}

digit = 1 → {3: 2, 2: 2, 1: 1}
digit = 1 → {3: 2, 2: 2, 1: 2}

"""