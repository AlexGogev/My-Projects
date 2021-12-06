import tkinter

window = tkinter.Tk()
window.minsize(250,100)
window.title("Miles to Km")

miles = tkinter.Entry(text="Miles")
miles.grid(column=1, row=0)

miles_title= tkinter.Label(text="Miles")
miles_title.grid(column=2, row=0)

equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=2)

equal_to = tkinter.Label(text="0")
equal_to.grid(column =1, row=2)

km = tkinter.Label(text="Km")
km.grid(column =2 , row=2)


def convert():
    miles_to_convert = miles.get()
    new_val = int(miles_to_convert) * 1.60934
    equal_to["text"] = round(new_val, 3)


button = tkinter.Button(text="Calculate", command= convert)
button.grid(column=1, row=1)
window.mainloop()