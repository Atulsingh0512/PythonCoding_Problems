def is_prime(num):
    if num < 2:
        return "Not Prime"

    for i in range(2, int(num ** 0.5) + 1): #Check whether num is divisible by any number from 2 up to √num.
        if num % i == 0:
            return "Not Prime"

    return "Prime"


num = 6

result = is_prime(num)

print("Input number:", num)
print("Result:", result)