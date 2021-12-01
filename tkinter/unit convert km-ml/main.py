import tkinter

window = tkinter.Tk()  #create window
window.title("my first GUI")
window.minsize(width=600, height=600)


#label
label = tkinter.Label(text="hi am label", font=("Ariel", 24))
label.pack(side="top")

label["text"] = "Label"

#button

inputing = tkinter.Entry(width=100 )
inputing.pack()

def button_clicked():    
    text = inputing.get()
    label["text"]  = text
    



button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()


#entry
"""
inputing = tkinter.Entry(width=100 )
inputing.pack()
inputing.get()

"""


window.mainloop()