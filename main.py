from tkinter import *
from tkinter import messagebox
import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def passw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for _ in range(nr_letters)]
    password_list2 = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_list1 + password_list2 + password_list3

    random.shuffle(password_list)

    password = "".join(password_list)
    entry3.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(entry1.get()) < 1 or len(entry3.get()) < 1:
        messagebox.showinfo(title="oops", message="you cant leave empty")
    else:
        is_ok = messagebox.askokcancel(title=entry1.get(),
                                       message=f"These are your entered details: \n email: {entry2.get()}\n "
                                               f"password:{entry3.get()}")
        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()} \n")
            entry1.delete(0, 'end')
            entry3.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label1.config(pady=5)
entry1 = Entry(width=53)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label2.config(pady=5)
entry2 = Entry(width=53)
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(0, "pragadajayasree@gmail.com")

label3 = Label(text="Password:")
label3.grid(row=3, column=0)
label3.config(pady=5)
entry3 = Entry(width=34)
entry3.grid(row=3, column=1)
button1 = Button(text="Generate Password", command=passw)
button1.grid(row=3, column=2)

button2 = Button(text="Add", width=45, command=save)
button2.grid(row=4, column=1, columnspan=2)

window.mainloop()
