import random
import pandas
from tkinter import *
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
french_word = ""

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def random_word_generator():
    global french_word, flip_timer
    window.after_cancel(flip_timer)
    french_word = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(french_text, text=french_word["French"], fill="black")
    flip_timer = window.after(3000, func=countdown)


def countdown():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(french_text, text=french_word["English"], fill="white")

def known_word():
    #.remove removes both selected items in a list eg.[{French: police, English: Police}]
    to_learn.remove(french_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    #my code
    #french_words = data["French"]
    #french_words_left = french_words.values.tolist()
    #french_words_left.remove(french_word["French"])
    #english_words = data["English"]
    #english_words_left  = english_words.values.tolist()
    #english_words_left.remove(french_word["English"])
    #df = pandas.DataFrame({"French":french_words_left, "English": english_words_left})
    #df.to_csv("data/words_to_learn.csv", index=False)
    random_word_generator()


#UI interface
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#timer
flip_timer = window.after(3000, func=countdown)

canvas = Canvas(height=526, width=800)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

#half of canvas
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
french_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

tick = PhotoImage(file="images/right.png")
correct_button = Button(image=tick,bg= BACKGROUND_COLOR, highlightthickness=0, command=known_word)
correct_button.grid(row=1, column=0)

cross = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross, bg= BACKGROUND_COLOR, highlightthickness=0, command=random_word_generator)
wrong_button.grid(row=1, column=1)

random_word_generator()
window.mainloop()
