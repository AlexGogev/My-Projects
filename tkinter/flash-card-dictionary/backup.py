from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

to_learn_lang = "Bulgarian"
source = "Bulgarian"
data = pandas.read_csv(f"data/{to_learn_lang}.csv")


def switch_es():
    global source, to_learn_lang, data
    source = "Spanish"
    to_learn_lang= "words_to_learn_spanish"
    data = pandas.read_csv("data/Spanish.csv")
    
    
def switch_bg():
    global source, to_learn_lang, data
    source = "Bulgarian"
    to_learn_lang= "words_to_learn_bulgarian"
    data = pandas.read_csv("data/Bulgarian.csv")
    


try:
    data 
except FileNotFoundError:
    original = pandas.read_csv(f"data/{source}.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")





def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text =f"{source}", fill="black")
    canvas.itemconfig(card_word, text =current_card[f"{source}"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer =window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data =pandas.DataFrame(to_learn)
    data.to_csv(f"data/words_to_learn_{source}.csv", index=False)
    next_card()




window = Tk()
window.title("Dictionary Game")
window.config(padx=50, pady=5, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#canvas allow to lay one over another
canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img) #x and y must be given
card_title = canvas.create_text(400, 150,text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 45, "bold"))

#removes background color - give same as window bg color
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command=next_card)
unknown_button.grid(row=2, column=0)


check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0,command=is_known)
known_button.grid(row=2, column=1)

es = Button(text="es",width =30, command=switch_es)
es.grid(row=0, column=0)
bg = Button(text="bg",width =30, command=switch_bg)
bg.grid(row=0, column=1)



next_card()
window.mainloop()

