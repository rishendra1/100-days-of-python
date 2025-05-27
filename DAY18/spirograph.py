from turtle import Turtle
import random
colors = ["red", "green", "blue", "magenta", "cyan"]
timmy = Turtle()
timmy.pensize(3)
def draw_square():
    for i in range(4):
       timmy.color(random.choice(colors))
       timmy.forward(100)
       timmy.right(90)
for j in range(100):
    draw_square()
    timmy.left(30)
