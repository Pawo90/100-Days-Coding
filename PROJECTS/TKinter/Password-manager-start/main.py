from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    # Load data from *.json file
    try:
        with open("passwords.json", "r") as data_file:
            # Read/load *.json file
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")

    else:
        website = website_entry.get()
        if len(website) == 0:
            messagebox.showerror(title="Website", message="Website name field is empty!")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}\n")
            else:
                messagebox.showinfo(title="Error",
                                    message=f"""No details for "{website}" exists.""")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0:
        messagebox.showerror(title="Website", message="Website field is empty!")
    elif len(password) == 0:
        messagebox.showerror(title="Password!", message="Password field is empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email/user: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Is this data OK?")

        if is_ok:
            # Try to update *.json file
            try:
                with open("passwords.json", "r") as data_file:
                    # Read/load *.json file
                    data = json.load(data_file)
            # If file not exist - create file and save data
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    # Save data to *.json file
                    json.dump(new_entry, data_file)
            # If file exist - save updated data
            else:
                # Update *.json file with new data
                data.update(new_entry)
                with open("passwords.json", "w") as data_file:
                    # Save data to *.json file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# region Writing data to *.txt file method
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#
#
#     if website == "":
#         messagebox.showerror(title="Website", message="Website field is empty!")
#     elif password == "":
#         messagebox.showerror(title="Password!", message="Password field is empty!")
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"Email/user: {email}\n"
#                                                               f"Password: {password}\n"
#                                                               f"Is this data OK?")
#
#         if is_ok:
#             with open("passwords.txt", "a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
# endregion


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)


# Labels ----------------------------------------------------

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="w")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")


# Entries ----------------------------------------------------

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "pawelp1990@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")


# Buttons ----------------------------------------------------

button_search = Button(text="Search", width=15, command=find_password)
button_search.grid(row=1, column=2, sticky="EW")

button_generate = Button(text="Generate Password", width=15, command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=35, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
