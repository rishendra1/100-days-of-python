def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum

result = add(1,2,3,4,5,6,7,8,9)
print(result)