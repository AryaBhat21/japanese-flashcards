from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#---------UI SETUP ---------------#
window=Tk()
window.title("Japanese-Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas for flashcard
canvas=Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)



window.mainloop()