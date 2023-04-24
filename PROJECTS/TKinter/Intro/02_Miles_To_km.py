from tkinter import *

window = Tk()
window.title("Miles to km coverter")
window.minsize(300, 100)
window.config(padx=20, pady=20)

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

label_miles_text = Label(text="Miles")
label_miles_text.grid(column=2, row=0)

result_desc_text = Label(text="is equal to")
result_desc_text.grid(column=0, row=1)

label_result = Label(text=" ")
label_result.grid(column=1, row=1)

label_km_text = Label(text="km")
label_km_text.grid(column=2, row=1)


def calculate():
    calculations = float(input_miles.get()) * 1.609
    label_result.config(text=calculations)


button_calc = Button(text="Calculate", command=calculate)
button_calc.grid(column=1, row=2)


window.mainloop()
