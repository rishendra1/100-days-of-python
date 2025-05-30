from turtle import Turtle, Screen
import random

import turtle
turtle.colormode(255)

timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()# hides the arrow

color_list = [
    (239, 246, 241), (245, 240, 235), (236, 239, 243), (240, 234, 215),
    (202, 165, 109), (149, 75, 50), (222, 201, 136), (53, 93, 123),
    (170, 154, 41), (135, 31, 20), (134, 163, 184), (197, 91, 71),
    (48, 122, 86), (145, 178, 148), (14, 98, 70), (232, 176, 165),
    (160, 144, 157), (55, 45, 50), (101, 75, 77), (183, 205, 171),
    (36, 60, 74), (19, 86, 90), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (106, 127, 153), (174, 94, 97), (116, 33, 43),
    (237, 170, 160), (222, 177, 179)
]


def hirst_paint(grid_size):
    timmy.setheading(0)
    x_start = -grid_size * 25
    y_start = -grid_size * 25
    timmy.goto(x_start, y_start)

    for row in range(grid_size):
        for col in range(grid_size):
            timmy.dot(20, random.choice(color_list))
            timmy.forward(50)
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(50 * grid_size)
        timmy.setheading(0)
hirst_paint(10)
screen = Screen()
screen.exitonclick()
