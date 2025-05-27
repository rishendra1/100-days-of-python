from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(2)
timmy.speed("fastest")
def draw_spirograph(size):
    for i in range(int(360 / size)):
       timmy.color("black")
       timmy.circle(100)
       timmy.right(12)
draw_spirograph(2)
screen = Screen()
screen.exitonclick()