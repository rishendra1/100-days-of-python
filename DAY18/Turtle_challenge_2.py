from turtle import Turtle, Screen

timmy = Turtle()
timmy.pensize(3)
def traverse():
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
for i in range(20):
    traverse()
screen = Screen()
screen.exitonclick()
