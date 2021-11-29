import tkinter

window = tkinter.Tk()  #create window
window.title("my first GUI")
window.minsize(width=600, height=600)

label = tkinter.Label(text="hi am label", font=("Ariel", 24))
label.pack(side="top")








window.mainloop()