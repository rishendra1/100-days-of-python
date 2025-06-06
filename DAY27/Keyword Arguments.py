def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiplication"]
    return n
result = calculate(3,add=4,multiplication=5)
print(result)