import tkinter
import time
from tkinter import messagebox
import pyperclip
import random
import json
#write dump(), reed load(), update update()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- SEARCH GENERATOR ------------------------------- #
def search():
    try:
        with open("pass.json" ,"r") as json_file:
            data = json.load(json_file)
        
        messagebox.showinfo(title="Details", message=f'Email: {data[website_entry.get()]["email"]} \nPassword:{data[website_entry.get()]["password"]}\nPassword copied to clipboard')
        pyperclip.copy(data[website_entry.get()]["password"])
    except KeyError:
        messagebox.showinfo(title="No info", message="Not avalable")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

rand_pass = []
password = ""
def generate_password():

    for i in range(8):
        rand_pass.append(random.choice(letters))
    for i in range(2):    
        rand_pass.append(random.choice(symbols))
        rand_pass.append(random.choice(symbols))
    password= "".join(rand_pass)
    password_entry.insert(0, password) 
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def create_label():
    confirm_label = tkinter.Label(text="Saved!", font="Ariel")
    confirm_label.grid(row=5, column=1)
    

def save_it():
    web = website_entry.get()
    email = email_entry.get()
    paswd= password_entry.get()
    new_data = {
        web: {
        "email":email,
        "password":paswd
        }
    }
    
    if len(web) > 0 and len(email) > 0 and len(paswd) >0:
            
        #load data
        try:
            with open("pass.json","r") as data_file:
                #reeding old data
                data = json.load(data_file)
                
           
        except FileNotFoundError:
            #save data or create file ("w")
            with open("pass.json", "w") as data_file:
                #saving updated data
                json.dump(new_data, data_file, indent=4)

                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                create_label()
                rand_pass.clear()
        else:
            #update data
            data.update(new_data)
            with open("pass.json", "w") as data_file:
                
                #saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            create_label()
            rand_pass.clear()

    else:
        messagebox.showinfo(title="Error", message="Cannot be blank")
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


website_entry = tkinter.Entry(width=36)
website_entry.focus() #focus cursor on startup
search_button = tkinter.Button(text="Search", width=15, command=search)

email_entry = tkinter.Entry(width=55)
email_entry.insert(0, "myemail@aol.com") #2 parameters -> index and string
password_entry= tkinter.Entry(width=36)

website_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)     
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, )

#buttons
generate_pass = tkinter.Button(text="Generate password", command=generate_password)
generate_pass.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=26, command=save_it)
add_button.grid(row=4, column=0,columnspan=3, pady=15, padx=15)





window.mainloop()


