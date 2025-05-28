from turtle import Turtle, Screen
import random
screen = Screen()
is_race_on = False
screen.setup(600,600)
user_choice = screen.textinput(title = "Welcome", prompt = "Which coloured turtle will win the race? ")
colors = ['yellow','green','red','black']
y_positions = [-100, -50, 0 , 50]
all_turtles = []
for turtle_index in range(4):
    timmy = Turtle(shape='turtle')
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x = -250,y = y_positions[turtle_index])
    all_turtles.append(timmy)
if user_choice:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            colour = turtle.pencolor()
            if colour == user_choice:
                print("Congratulations! You won!")
                exit()
            else:
                print(f"Sorry! You lost! {colour} is the winner`")
                is_race_on = False
        distance = random.randint(1,10)
        turtle.forward(distance)