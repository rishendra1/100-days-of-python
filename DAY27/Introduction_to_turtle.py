import tkinter as tk  # Best practice to alias tkinter

# Create main window
window = tk.Tk()
window.title("My first GUI code")
window.minsize(width=450, height=500)

# Create a label
label = tk.Label(text="Hello friends!!!", font=("Arial", 20, "bold"))
label.place(x=100, y=100)
#place is used to x and y coordinate
# Function to be called on button click
def button_clicked():
    label.config(text="Button Clicked!")

# Create a button
button = tk.Button(text="Click", command=button_clicked)
button.place(x=150, y=150)

in_put = tk.Entry()
in_put.place(x=150, y=200)
in_put.grid(row=4, column=5)


# Run the GUI loop
window.mainloop()
