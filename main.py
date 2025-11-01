from tkinter import *
import math

# ----------------------- CONSTANTS -------------------------------------- #
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

# ----------------------- TIMER RESET --------------------------- #
def reset_timer():
    screen.after_cancel(timer)
    canva.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# --------------------TIMER MECHANISM ---------------------------#
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)

# -------------------------COUNTDOWN MECHANISM ---------------------#
def count_down(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canva.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")

    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        check_marks.config(text=mark)

# --------------------------------- UI SETUP ------------------------ #
screen = Tk()
screen.title("Pomodoro App")
screen.config(padx=100, pady=50, bg=YELLOW)

# Timer Heading
title_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(row=0, column=1)

# Canvas with Tomato Image
canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Projects/TkinterPomodoroApp/images.png")
canva.create_image(100, 112, image=tomato_img)
timer_text = canva.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canva.grid(row=1, column=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer, width=8,bg="#e7305b",fg="#ffffff", borderwidth=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, width=8, bg="#9bdeac", fg="#ffffff", borderwidth=0)
reset_button.grid(row=2, column=2)

# Check Marks
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_marks.grid(row=3, column=1)

screen.mainloop()
