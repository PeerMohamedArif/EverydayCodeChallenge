from tkinter import *
import pandas
import random
current_card={}
flip_timer=None
BACKGROUND_COLOR = "#B1DDC6"
french_words_data={}

# -------------------- CREATE NEW FLASH CARDS -------------------- #
try:
    data=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("french_words.csv")
    french_words_data=original_data.to_dict(orient="records")
else:
    french_words_data=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer

    window.after_cancel(flip_timer)

    current_card=random.choice(french_words_data)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=flash_card_front)

    flip_timer = window.after(ms=3000, func=flip_the_card)


def flip_the_card():
    canvas.itemconfig(card_background,image=flash_card_back)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")

def is_known():
    french_words_data.remove(current_card)
    pandas.DataFrame(french_words_data).to_csv("words_to_learn.csv",index=False)
    next_card()



# -------------------- CREATING THE UI -------------------- #
window=Tk()
window.title("FlashCard App")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

flip_timer=window.after(ms=3000,func=flip_the_card)

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

wrong_image=PhotoImage(file='images/wrong.png')
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

canvas=Canvas(width=800,height=526)
flash_card_front=PhotoImage(file='images/card_front.png')
flash_card_back=PhotoImage(file='images/card_back.png')
card_background=canvas.create_image(400,263,image=flash_card_front)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)


card_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="Word",font=("Ariel",60,"italic"))

canvas.grid(row=0, column=0, columnspan=2)
next_card()

window.mainloop()