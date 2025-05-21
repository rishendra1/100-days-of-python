def is_palindrome(n):
    rev = 0
    c = n
    while (n != 0):
        i = n % 10
        rev = rev * 10 + i
        n = n // 10
    if c==rev:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"The number {number} is a palindrome.")
else:
    print(f"The number {number} is not a palindrome.")