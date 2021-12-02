import tkinter
from tkinter import font
import math
from typing import Text
# ---------------------------- CONSTANTS ------------------------------- #

#canvas - allows to put images on top of other widgets. Widgets on widgets
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

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0 :
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        title.config(text="WORK", fg=GREEN)

    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            mark += "✓"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

#https://colorhunt.co/ for colors 

window = tkinter.Tk()
window.config(padx=100, pady=50, bg=YELLOW)



title= tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW ,font=(FONT_NAME, 50), ) #fg -> fore ground
title.grid(column=1, row=0)

canvas = tkinter.Canvas(width=240 ,height=244, bg=YELLOW, highlightthickness=0) #highlightthickness -> removes border of the image
tomato_img = tkinter.PhotoImage(file="tomato.png") #reeds file
canvas.create_image(103, 112, image=tomato_img) #req x,y
timer_text = canvas.create_text(103,122, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)





window.title("Pomodoro")








window.mainloop()