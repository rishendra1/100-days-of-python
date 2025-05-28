def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def calculator(a, b, fun):
    return fun(a, b)
result = calculator(22,17 , subtraction)
print(result)