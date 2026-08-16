def prime_numbers_in_range(start, end):
    result = []

    for num in range(start, end + 1):
        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            result.append(num)

    return result


# Example Input
start = 10
end = 30

# Function Call
result = prime_numbers_in_range(start, end)

# Output
print("Start:", start)
print("End:", end)
print("Prime numbers:", result)


# Expected Output:
# Start: 10
# End: 30
# Prime numbers: [11, 13, 17, 19, 23, 29]