def fib(n):
    a = 0
    b = 1
    if n == 1: return a
    if n == 2: return b
    if n > 2 : return fib(n - 1) + fib(n - 2)

n = int(input("No. of terms you need to print - "))
print("Terms in Fibonacci series are :")
for i in range(1,n + 1):
    print(fib(i))


