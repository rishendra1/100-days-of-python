def is_prime(n):
    count = 0
    for i in range(2,n):
        if(n % i) == 0:
            count = count + 1
    if count == 0:
        return True
    else:
        return False
number = int(input("Enter a number - "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")