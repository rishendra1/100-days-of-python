# 100-days-of-python
# "My 100-day journey of learning Python, building projects, and solving problems.”
1. Python is a high level language
2. Python consists of many built-in functions
3. round(Number , number_of_decimal_digits) helps in rounding of digit in given no. of decimal places
4. To write keywords, we must follow some rules,
    b. Name must start with a "Letter" or "_"
    c. Can contain numbers , underscrolls
5. "print()" is a function in python that is used to print / display the output on the screen
6. Python primitive data types
      1. int
      2. float
      3. string
      4. tuples
      5. Lists
      6. Dictionaries
7. String is a group of characters that are enclosed by "" (or) ''
8. "len()" gives the length of the given string
9. "print(str_name.upper())" prints the string in Uppercase, where str_name is the name of the string
10. "print(str_name.lower())" prints the string in Lowercase, where str_name is the name of the string
11. Comparison Operators:
    1. ">" - greater than
    2. "<" - less than
    3. "<=" - less than or equal to
    4. ">=" - Greater than or equal to
    5. "==" - Equal to
    6. "!=" - Not Equal to
12. if <"this condition is true">:
         <"then execute this condition">
    else:
         <"then execute this condition">
13. Arithmetic Operators:
    1. '+' - Addition
    2. '-' - Subtraction
    3. '*' - Multiplication
    4. '/' - Divison
    5. '%' - Modulo
    6. '**' - Exponent
    7. '//' - Integral division
14. Logical Operators:
    1. "and"
       1. True and True becomes - True
       2. True and False becomes - False
       3. False and True becomes - False
       4. False and False becomes - True
    2. "or"
       1. True or True becomes - True
       2. True or False becomes - True
       3. False or True becomes - True
       4. False or False becomes - False
    3. "not" - operator
15. " import random " makes use of random module in your code
16. "random.randint(a , b)" returns a random number between a and b
17. "import File_name" helps us to to import another python file into the existing python file
18. "random.random()" helps us to return a random floating point number(0 to 1)
19. "random.uniform(a,b)" returns a floating point number between a and b
20. Lists are one of the data types in python used to store different items of any data type
21. Lists are denoted as '[]'
22. These are also accessed by using indexes
23. "List_Name.append(Variable)" - adds a variable to the list
24. "List_Name.extend([V1,V2,V3.......])" - adds a bunch of variables to the list
25. "List_Name.insert(i , x)" inserts variable "x" in the 'i'th position
26. "List_Name.remove(x)" removes the variable "x" if it is present in the List
27. "List_Name.pop(i)" removes the variable whose index is "i"
28. "random.choice(List_Name)" returns the random variable from the list
29. Loops allow us to tell the computer to repeat actions without having to write the code.
30. "for i in range(a , b , n) " means "i" starts from and increments by "n" till "b"
31. If "My_List" is of list data type and if you want to convert into array then do, "ARRAY = "".join(My_List)
32. Function in its simplest form is just a wrapper name for a block of code
33. While syntax:
    while <condition_is_true>:
          #Do something repeatedly
34. Dictionary = {key : value}
35. "max(Dictionary_Name.values())" denotes the maximum value in dictionary
36. In dictionary we can modify the existing items into new items
37. We can use docstrings to write multiline comments that describe our code
38. Example --> ''' My name is Rishendra
                    I am studying B.Tech'''
39. To debug a code,
    1. To describe a problem
    2. Reproduce the bug - some bugs are sneaky, they only occur at one condition
    3. Play computer and evaluate each line
    4. Fix the errors
    5. Squash the bug with print statement - It can helps us expose the hidden values while your code is running
    6. Using a debugger
    7. Take a break and think
    8. Ask a friend
40. In Python, ValueError is an exception raised when a function receives an argument of the correct data type but an inappropriate value.(Invalid data type)
41. a , b = random.sample(list, 2) - gives 2 different choices
42. OOP - Object Oreinted Programming
43. To map with the real world scenarios, we started using objects in the code, this is called as Object Oriented Programming
44. These are procedural and functional
45. "class" is a blueprint for creating objects
46. All classes have a function called __init__(), which is always executed when class is initialized
47. For example:
    #creating class
    class Student:
        def __init__(self,fullname):
            self.name = fullname
    #self is a reference to the current instance of the class and it helps to access the variables to the class, that belongs to the class
    #creating object
    s1 = student("Karan")
    print(s1.name)
48. "from turtle import Turtle, Screen" imports the turtle library    
49. Turtle_name.shape("turtle") - prints the shape of turtle
50. Turtle_name.color("Color_name") - adds the colour to the shape
51. screen_name.bgcolor("Color_name") - adds assigned color to the background
52. screen_name.exitonclick() - "Output exits when we click on the output
53. turtle_name.forward(number) - moves by the number of places
54. ".left(angle)" - changes the position to he angle
55. ".pensize(number)" - used to have a particular size
56. "penup()" - we stop to draw the line
57. "pendown()" - to draw the line
58. "setheading()" is a function used in turtle graphics to set the orientation, or direction, the turtle is facing.
59. Python Tuples - (v1,v1,v3.......) - where v1,v2,v3 are some values
60. In tuples, we can't change the existing values
61. "colormode(value)" - turtle colormode to allow RGB values from 0 - value
62. "hideturtle()" hides the arrow pointer
63. Methods are the functions that belongs to the objects
64. Staric methods are the functions that don't use the self parameter
65. Abstraction: Hiding the implementation details of the class , showing the essential features to the user
66. Encapsulation: Wrapping of data and functions into a single unit
67. Private attributes and methods are meant to be used within the class and are not accessible outside the class
68. Inheritance: When one class derives the properties of the another class
69. Inheritance are of 3 types:
    1. Single : A child class inherits from only one parent class.
    2. Multi-level: A class is derived from a class which is also derived from another class.
    3. Multiple: A child class inherits from more than one parent class.
70. super() method is used to access the methods of parent class
71. 
