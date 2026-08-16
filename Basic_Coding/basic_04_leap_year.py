def is_leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not a Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    return "Not a Leap Year"


year = 2024

result = is_leap_year(year)

print("Year:", year)
print("Result:", result)