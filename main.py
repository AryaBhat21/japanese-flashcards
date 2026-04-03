from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT=("Ariel", 40, "italic")
WORD_FONT=("Ariel", 60, "bold")

window=Tk()

card_front_img=PhotoImage(file="images/card_front.png") #needs Tk() to be created before using PhotoImage
card_back_img=PhotoImage(file="images/card_back.png")

#---------UI SETUP ---------------#
#window=Tk() -> at the top because it creates the main window to use PhotoImage and other widgets. It should be before any widget creation.
window.title("Japanese-Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas for flashcard
canvas=Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
#load and position of image
canvas_image=canvas.create_image(400, 263,image=card_front_img)

#card text
card_title=canvas.create_text(400,150,text="Japanese",font=TITLE_FONT)
card_word=canvas.create_text(400,263,text="word", font=WORD_FONT)
canvas.grid(row=0,column=0,columnspan=2)

#known button
check_image=PhotoImage(file="images/right.png")
known_button=Button(image=check_image,highlightthickness=0)
known_button.grid(row=1, column=0)

#unknown button
wrong_image=PhotoImage(file="images/wrong.png")
known_button=Button(image=wrong_image,highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()