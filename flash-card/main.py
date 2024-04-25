from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
to_learn = {}

try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# data_file = {row.french: row.english for (index, row) in data.iterrows()}

current_card = {}

def is_known():

    to_learn.remove(current_card)
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/word_to_learn.csv", index=False)
    next_card()

def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    front_canvas.itemconfig(title_text, text="French", fill="black")
    front_canvas.itemconfig(word_text, text=current_card["french"], fill="black")
    front_canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    front_canvas.itemconfig(title_text, text="English", fill="white")
    front_canvas.itemconfig(word_text, text=current_card["english"], fill="white")
    front_canvas.itemconfig(card_background, image= card_back_image)

window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

front_canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = front_canvas.create_image(400, 263, image=card_front_image)
front_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = front_canvas.create_text(400, 100, text=f"Title", fill="black", font=("Ariel", 35, "italic"))
word_text = front_canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 35, "bold"))
front_canvas.grid(column=0, row=0, columnspan=2)


wrong_png = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_png, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_png = PhotoImage(file="./images/right.png")
correct_button = Button(image=right_png, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)
next_card()

window.mainloop()
