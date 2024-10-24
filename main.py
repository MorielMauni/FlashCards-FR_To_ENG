# ---------------------------- IMPORTS & VARIABLES ------------------------------- #
from tkinter import *
import pandas
import random
current_card = {}
to_learn = {}
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- READ CSV ------------------------------- #
try:
    data = pandas.read_csv("./data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") # Creats lists of dictioneris

# ---------------------------- BUTTONS COMMENDS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    white_canvas.itemconfig(card_title, text="French", fill="black")
    white_canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    white_canvas.itemconfig(card_bg, image=card_front)
    flip_timer = flip_timer = window.after(3000, func=flip_card)

def is_know():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
# ---------------------------- SWITCH TO ENG ------------------------------- #
def flip_card():
    global current_card
    white_canvas.itemconfig(card_title, text="English", fill="white")
    white_canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    white_canvas.itemconfig(card_bg, image=card_back)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

white_canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="./image/card_front.png")
card_back = PhotoImage(file="./image/card_back.png")
card_bg = white_canvas.create_image(400, 263, image=card_front)
card_title = white_canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = white_canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
white_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
white_canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./image/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="./image/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
