from tkinter import *


def clear_fields():
    website_entry.delete(0, END)
    Email_entry.delete(0, END)
    Password_entry.delete(0, END)
def save():
    web = website_entry.get()
    user_name = Email_entry.get()
    p = Password_entry.get()

    if len(web) == 0 or len(user_name) == 0 or len(p) == 0:
        print("Enter valid input")
        return
    with open("Data.txt","a") as f:
        f.write(f"{web} || {user_name} || {p} \n")
    clear_fields()

window = Tk()
window.title("Password Generator")
window.config(padx = 200, pady = 20)
canvas = Canvas(window, width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = photo)
canvas.grid(row=0,column=1)
website = Label(window,text="Website:")
website.grid(row=1)
email = Label(window,text="Email/Username:")
email.grid(row=2)
Password = Label(window,text="Password:")
Password.grid(row=3)
website_entry = Entry(window,width = 30)
website_entry.grid(row=1,column=1,columnspan=2)
Email_entry = Entry(window,width = 30)
Email_entry.grid(row=2,column=1,columnspan=2)
Password_entry = Entry(window,width = 30)
Password_entry.grid(row=3,column=1,columnspan=2)

password_button = Button(window,text="Save Password",command=save)
password_button.grid(row=3,column=2)
add_button = Button(window,text="clear",command=clear_fields)
add_button.grid(row=4,column=1)
window.mainloop()