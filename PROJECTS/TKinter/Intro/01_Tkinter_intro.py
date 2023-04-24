from tkinter import *

window = Tk()
window.minsize(500, 400)

label = Label(text="I am init label")
label.grid(column=0, row=0)


def change_text():
    label.config(text=input.get())


button_1 = Button(text="Button_1", command=change_text)
button_1.grid(column=1, row=1)

button_2 = Button(text="Button_2", command=change_text)
button_2.grid(column=2, row=0)


input = Entry(width=50)
input.grid(column=3, row=3)


window.mainloop()
