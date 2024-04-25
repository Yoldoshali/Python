from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    status_label.config(text="Timer")
    checkmark_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    global reps
    if reps % 2 == 1:
        count_down(WORK_MIN)
        status_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        status_label.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN)
        status_label.config(text="Break", fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    global reps
    count_min = count // 60
    count_sec = count % 60
    if count_min == 0 or count_min < 10:
        count_min = f"0{count_min}"
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        reps += 1
        if reps % 2 == 0:
            checkmark_count = (reps // 2) * "✓"
            checkmark_label.config(text=checkmark_count)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# window.after(1000, say_something, 1, 2, 3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

status_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
status_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
