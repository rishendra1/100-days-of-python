from tkinter import *

def click():
    label.config(text=f"Selected: {r.get()}")

window = Tk()
window.title("T")

r = IntVar()
r.set(2)

Radiobutton(window, text="A", variable=r, value=1, command=click).pack()
Radiobutton(window, text="B", variable=r, value=2, command=click).pack()
Radiobutton(window, text="C", variable=r, value=3, command=click).pack()
Radiobutton(window, text="D", variable=r, value=4, command=click).pack()

label = Label(window, text=f"Selected: {r.get()}")
label.pack()

window.mainloop()
