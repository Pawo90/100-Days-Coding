from tkinter import *

window = Tk()

label = Label(text="I am init label")
label.pack()


def change_text():
    label.config(text=input.get())


button = Button(text="Change label text", command=change_text)
button.pack()


input = Entry(width=50)
input.pack()


window.mainloop()
