from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

screen.title("Snake Game")

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)
screen.update()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)
    

