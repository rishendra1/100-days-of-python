from tkinter import *
from tkinter import messagebox

def clear_fields():
    website_entry.delete(0, END)
    Email_entry.delete(0, END)
    Password_entry.delete(0, END)

def save():
    web = website_entry.get()
    user_name = Email_entry.get()
    p = Password_entry.get()

    if len(web) == 0 or len(user_name) == 0 or len(p) == 0:
        messagebox.showwarning("Input Error", "Enter valid input in all fields.")
        return

    with open("Password_data.txt", "a") as f:
        f.write(f"{web} || {user_name} || {p}\n")

    clear_fields()
    messagebox.showinfo("Saved", "Password saved successfully!")

def search_website():
    web = website_entry.get()
    found = False

    try:
        with open("../DAY29/Data.txt", "r") as f:
            for line in f:
                if line.lower().startswith(web.lower()):
                    messagebox.showinfo("Password Found", line.strip())
                    found = True
                    break

        if not found:
            messagebox.showerror("Password Not Found", "Please enter a valid website.")
    except FileNotFoundError:
        messagebox.showerror("File Error", "Password data file not found.")

window = Tk()
window.title("Password Generator")
window.config(padx=200, pady=20)

canvas = Canvas(window, width=200, height=200)
photo = PhotoImage(file="../DAY29/logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)


Label(window, text="Website:").grid(row=1, column=0)
Label(window, text="Email/Username:").grid(row=2, column=0)
Label(window, text="Password:").grid(row=3, column=0)

website_entry = Entry(window, width=20)
website_entry.grid(row=1, column=1)
Email_entry = Entry(window, width=30)
Email_entry.grid(row=2, column=1, columnspan=2)
Password_entry = Entry(window, width=30)
Password_entry.grid(row=3, column=1)

search_button = Button(window, text="Search", command=search_website)
search_button.grid(row=1, column=2)
password_button = Button(window, text="Save Password", command=save)
password_button.grid(row=3, column=2)
add_button = Button(window, text="Clear", command=clear_fields)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
