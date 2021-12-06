import tkinter
import time
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def create_label():
    confirm_label = tkinter.Label(text="Saved!", font="Ariel")
    confirm_label.grid(row=5, column=1)
    

def save_it():
    with open("pass.txt","a") as filetext:
        web = website_entry.get()
        email = email_entry.get()
        paswd= password_entry.get()

        filetext.write(f"web: {web} |  email: {email} | pass: {paswd} \n")
        website_entry.delete(0, "end")
        password_entry.delete(0, "end")
        create_label()
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pass manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
email_label = tkinter.Label(text="Email/Username:")
password_label = tkinter.Label(text="Password:")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)


website_entry = tkinter.Entry(width=55)
website_entry.focus() #focus cursor on startup

email_entry = tkinter.Entry(width=55)
email_entry.insert(0, "myemail@aol.com") #2 parameters -> index and string
password_entry= tkinter.Entry(width=37)

website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, )

#buttons
generate_pass = tkinter.Button(text="Generate password")
generate_pass.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36, command=save_it)
add_button.grid(row=4, column=1,columnspan=2)





window.mainloop()