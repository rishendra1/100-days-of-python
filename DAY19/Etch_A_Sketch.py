from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(50)

def move_backward():
    timmy.backward(50)

def move_left():
    timmy.left(90)
    timmy.forward(50)

def move_right():
    timmy.right(90)
    timmy.forward(50)

def clear_all():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_all, "c")
screen.exitonclick()
screen.mainloop()
