from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0


# Timer Reset
def reset_timer():
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    checkmark_label.config(text = "")
    global reps 
    reps = 0
    
# Timer Mechanism
def start_timer():
    global reps 
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0: 
        count_down(long_break_sec)
        title_label.config(
            text = "20 Min Break",
            fg = RED
            ) 
    
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(
            text = "5 Min Break",
            fg = PINK
            )
    
    else:
        count_down(work_sec)
        title_label.config(
            text = "Working",
            fg = GREEN
        )
    
# Countdown Mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(
        timer_text, 
        text = f"{count_min}:{count_sec}"
        )
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark_label.config(text = marks)
            
# UI Setup
window = Tk()
window.title("Pomodoro")
window.config(
    padx = 100, 
    pady = 50, 
    bg = YELLOW
    )

title_label = Label(
    text = "Timer",
    font = (FONT_NAME, 40, "bold"),
    bg = YELLOW,
    fg = GREEN
    )

title_label.grid(
    column = 1, 
    row = 0
    )

canvas = Canvas(
    width = 206, 
    height= 224, 
    bg = YELLOW, 
    highlightthickness = 0
    )

tomato_img = PhotoImage(file = "tomato.png")

canvas.create_image(
    103, 
    112, 
    image = tomato_img
    )

timer_text = canvas.create_text(
    103, 
    130, 
    text = "00:00", 
    fill = "white", 
    font = (FONT_NAME, 25, "bold")
    )

canvas.grid(
    column = 1,
    row = 1
    )


start_button = Button(
    text = "START",
    font = (FONT_NAME, 14),
    highlightthickness = 0,
    command = start_timer
    )
start_button.grid(
    column = 0, 
    row = 2
    )

reset_button = Button(
    text = "RESET",
    font = (FONT_NAME, 14),
    highlightthickness = 0,
    command = reset_timer
    )
reset_button.grid(
    column = 2,
    row = 2
    )

checkmark_label = Label(
    font = (FONT_NAME, 20),
    bg = YELLOW,
    fg = GREEN,
    )

checkmark_label.grid(
    column = 1,
    row = 3
    )

window.mainloop()