from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.title("Rishendra___Ruppa")

frame = LabelFrame(window,text="This is a frame",padx=50,pady=50)
frame.pack(padx=10,pady=10)

b = Button(frame,text="Click Me")
b2 = Button(frame,text="Don't Click Me")
b.grid(row=0,column=0)
b2.grid(row=1,column=0)
window.mainloop()