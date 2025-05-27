from turtle import Turtle

timmy = Turtle()
def draw_triangle():
    for i in range(3):
       timmy.forward(100)
       timmy.right(120)
def draw_square():
    for i in range(4):
       timmy.forward(100)
       timmy.right(90)
def draw_pentagon():
    for i in range(5):
        timmy.forward(100)
        timmy.right(72)
def draw_hexagon():
    for i in range(6):
        timmy.forward(100)
        timmy.right(60)
def draw_heptagon():
    for i in range(7):
        timmy.forward(100)
        timmy.right(51.43)
def draw_octagon():
    for i in range(8):
        timmy.forward(100)
        timmy.right(45)
def draw_nonagon():
    for i in range(9):
        timmy.forward(100)
        timmy.right(40)
def draw_decagon():
    for i in range(10):
        timmy.forward(100)
        timmy.right(36)
draw_triangle()
draw_square()
draw_pentagon()
draw_hexagon()
draw_heptagon()
draw_octagon()
draw_nonagon()
draw_decagon()