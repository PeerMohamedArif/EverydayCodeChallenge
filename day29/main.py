from tkinter import *
import random
import pyperclip
from tkinter import messagebox
FONT_NAME = "Courier"



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list=password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered \n {email}\n Password:"
                                                           f"{password}\n"
                                                     f"Is it OK to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg= 'white')


canvas=Canvas(width=200,height=200,bg='white',highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website1=Label(text="Website:",bg='white', font=(FONT_NAME, 10,'bold'))
website1.grid(row=1,column=0)

email1=Label(text="Email/Username:",bg='white', font=(FONT_NAME, 10,'bold'))
email1.grid(row=2,column=0)

password1=Label(text="Password:",bg='white', font=(FONT_NAME, 10,'bold'))
password1.grid(row=3,column=0)

website_entry = Entry(bg='white', width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(bg='white', width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"arifoct24@gmail.com")

password_entry = Entry(bg='white', width=21)
password_entry.grid(row=3, column=1, columnspan=1)


button1=Button(text="Generate Password",bg='white',width=15,highlightthickness=0,command=generate_password)
button1.grid(row=3,column=2)

button1=Button(text="Add",width=36,bg='white',highlightthickness=0,command=save)
button1.grid(row=4,column=1,columnspan=2)

window.mainloop()
