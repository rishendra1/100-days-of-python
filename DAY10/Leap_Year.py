def Calculate_Leap_Year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
Number = int(input("Enter a number: "))
print(Calculate_Leap_Year(Number))