'''This code is application on loops
if number is divisible by 3 , print "Fizz"
if number is divisible by 5 , print "Buzz"
if a number is divisible by both 3 and 5 , print "FizzBuzz"
'''
n = int(input("Enter a Number: "))
for i in range (1,n + 1):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    if i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)