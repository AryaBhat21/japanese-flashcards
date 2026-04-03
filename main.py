from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT=("Ariel", 40, "italic")
WORD_FONT=("Ariel", 60, "bold")

window=Tk()

card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")

current_card={}
flip_timer=None
to_learn=[]

#---READ DATA ------#
try:
    data_frame = pd.read_csv("data/words_to_learn.csv")
    if data_frame.empty:
        data_frame = pd.read_csv("data/japanese_words.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    data_frame = pd.read_csv("data/japanese_words.csv")

data = data_frame.to_dict(orient="records")
to_learn = data.copy()

#---RANDOM CARD -----#
def nextCard():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Done!", fill="black")
        canvas.itemconfig(card_word, text="All words learned!", fill="black")
        return  
    current_card=random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flipCard)

#---FLIP CARD -----#
def flipCard():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

#---remove known word from the list and save to csv file -----#
def is_known():
    global to_learn
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    nextCard()

#---------UI SETUP ---------------#
#window=Tk() used at top as it creates the main window to use PhotoImage and other widgets. It should be before any widget creation.
window.title("FLashy - French Edition")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas for flashcard
canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
#load and position the image
canvas_image=canvas.create_image(400,263,image=card_front_img)

#card text
card_title = canvas.create_text(400,150,text="Japanese", font=TITLE_FONT)
card_word = canvas.create_text(400,263,text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

#buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=nextCard)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

nextCard()
window.mainloop()