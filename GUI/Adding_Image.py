from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("T")
canvas = Canvas(window, width=200, height=224,highlightthickness=0)
Photo = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=Photo)
canvas.pack()
window.mainloop()