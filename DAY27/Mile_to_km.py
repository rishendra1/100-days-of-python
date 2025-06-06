from tkinter import *

def converter():
    miles = float(miles_input.get())
    km = miles * 1.609
    Kilometer_result_label.config(text=f"{km}")
window = Tk()
window.title("Mile to KM Converter")

miles_input = Entry(window)
miles_input.grid(row=0, column=1)
miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(window, text="is equal to")
is_equal_to_label.grid(row=1, column=0)
Kilometer_result_label = Label(window, text="0")
Kilometer_result_label.grid(row=1, column=1)
Kilometer_label = Label(window, text="Kilometers")
Kilometer_label.grid(row=1, column=2)
calculate_button = Button(window, text="Calculate",command=converter)
calculate_button.grid(row=2, column=1)

window.mainloop()