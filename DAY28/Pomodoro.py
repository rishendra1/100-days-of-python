from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=GREEN)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    #returns largest whole number
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work = range.floor(reps/2)
        for _ in range(work):
             mark = "✓"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50,bg=YELLOW)

title_label = Label(window, text="Timer", font=("Arial", 40, "bold"))
title_label.grid(row=0, column=1)
canvas = Canvas(window, width=200, height=224,highlightthickness=0,bg=YELLOW)
Photo = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=Photo)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME, 35, "bold"),fill="black")
canvas.grid(column=1, row=1)

start_button = Button(window, text="START", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(window, text="RESET", command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(window, text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
window.mainloop()