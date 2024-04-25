from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- Search Function ------------------------------- #
def search():
    website = (website_entry.get()).capitalize()
    try:
        with open("data.json", "r") as data_file:
            data_content = json.load(data_file)
    except:
        messagebox.showinfo(title='Error', message="No Data File Found")
    else:
        try:
            website_info = data_content[website]
        except KeyError:
            messagebox.showinfo(title=website, message="No Details for the website exists")
        else:
            messagebox.showinfo(title=website, message=f"Email: {website_info['email']}\nPassword : {website_info['password']}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_pass():

    letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I',
               'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't',
               'T', 'u',
               'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
    punctuation = '''!"#$%&\()*+,-./:;<=>?@[\]^_`{|}~'''
    digits = '0123456789'
    pass_letter = [choice(letters) for i in range(randint(8, 10))]
    pass_number = [choice(digits) for i in range(randint(2, 4))]
    pass_symbols = [choice(punctuation) for i in range(randint(2, 4))]
    pass_list = pass_letter + pass_symbols + pass_number
    shuffle(pass_list)
    ready_pass = ''.join(pass_list)
    password_entry.delete(0, END)
    password_entry.insert(0, ready_pass)
    pyperclip.copy(ready_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = (website_entry.get())
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website.capitalize(): {
        "email" : email,
        "password": password,
        }
    }

    #messagebox.showinfo(title="Title", message="message")
    if len(website) == 0 or len(email) == 0:
        messagebox.showwarning("Oops", message="Don't leave the field empty")
    else:
            #json.dump(new_data, data_file, indent=4)
            #data_content = json.load(data_file)
            #print(data_content)
            try:
                with open(file="data.json", mode="r") as data_file:
                    data_content = json.load(data_file)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data_content.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data_content, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)





    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
    #                                                           f"\n\nEmail: {email}\n\nPassword: {password} \n\n Is it ok to save ?")
    #     if is_ok:
    #         with open(file="data.txt", mode="a") as data:
    #             data.write(f"{website} | {email} | {password}\n")
    #             website_entry.delete(0, END)
    #             password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.config(pady=100, padx=70)


canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.config(padx=5, pady=5)
website_label.grid(column=0, row=1)
website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_label = Label(text="Email:")
email_label.config(padx=5, pady=5)
email_label.grid(column=0, row=2)
email_entry = Entry(width=56)
email_entry.insert(0, "yoldoshaliesonaliyev@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.config(padx=5, pady=5)
password_label.grid(column=0, row=3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", width=21, command=create_pass)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=49, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search",command=search, width=21)
search_button.grid(column=2, row=1)

window.mainloop()