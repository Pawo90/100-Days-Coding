from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TO_LEARN = "German"
TRANSLATED_LANGUAGE = "English"
PATH_TO_WORDS_FILE = "./data/german_words.csv"
# "./data/french_words.csv"
words_list = []
current_card = {}


# READ DATA FILE ----------------

def read_data_file():
    global words_list
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
    # Exception if file is empty
    except pd.errors.EmptyDataError:
        data = pd.read_csv(PATH_TO_WORDS_FILE)
    # Exception if file not exist
    except FileNotFoundError:
        data = pd.read_csv(PATH_TO_WORDS_FILE)

    words_list = data.to_dict(orient="records")


# BUTTONS FUNCTIONS ----------------

def is_known():
    global words_list, current_card
    if current_card in words_list:
        words_list.remove(current_card)
        data = pd.DataFrame(words_list)
        data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# PICK NEW CARD -----------------------------------

def next_card():
    global words_list, current_card, flip_timer

    current_card = random.choice(words_list)

    # Reset timer
    window.after_cancel("flip_timer")
    # Modify canvas
    card_canvas.itemconfig(card_title, text=LANGUAGE_TO_LEARN, fill="black")
    card_canvas.itemconfig(card_word, text=current_card[LANGUAGE_TO_LEARN], fill="black")
    card_canvas.itemconfig(card_image, image=card_front_img)
    # Start timer
    flip_timer = window.after(3000, flip_card)


def flip_card():
    card_canvas.itemconfig(card_title, text=TRANSLATED_LANGUAGE, fill="white")
    card_canvas.itemconfig(card_word, text=current_card[TRANSLATED_LANGUAGE], fill="white")
    card_canvas.itemconfig(card_image, image=card_back_img)


# WINDOW -----------------------------------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# TIMER -------------------------------------------------------------
read_data_file()
flip_timer = window.after(3000, flip_card)


# CANVAS ------------------------------------------------------------
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card_canvas = Canvas(width=800, height=526)

card_image = card_canvas.create_image(400, 263, image=card_front_img)
card_title = card_canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = card_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.grid(row=0, column=0, pady=20, columnspan=2)


# BUTTONS -----------------------------
btn_wrong_image = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=btn_wrong_image, highlightthickness=0)
btn_wrong.config(command=next_card)
btn_wrong.grid(row=1, column=0)

btn_right_image = PhotoImage(file="./images/right.png")
btn_right = Button(image=btn_right_image, highlightthickness=0)
btn_right.config(command=is_known)
btn_right.grid(row=1, column=1)

# Initialize first card
next_card()


window.mainloop()
