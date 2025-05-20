#To find greatest of three numbers
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
if a > b and a > c:
    print(a,"is greater than",b ,"and", c)
elif b > a and b > c:
    print(b,"is greater than",a ,"and", c)
else:
    print(c,"is greater than",a ,"and", b)
