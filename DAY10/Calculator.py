def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def function():
    print("Please select any option\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    option = int(input("Enter your choice: "))
    if option == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(addition(a, b), "is the answer")
    if option == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(subtraction(a, b), "is the answer")
    if option == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(multiplication(a, b), "is the answer")
    if option == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(division(a, b), "is the answer")
    if option > 4:
        print("Invalid option")
    n = input("Do you want to use the program again? -'Y' or 'N' - ")
    if n == "Y" or n == "y":
        function()
    else:
        print("Thank you for using this program")
        exit()
function()