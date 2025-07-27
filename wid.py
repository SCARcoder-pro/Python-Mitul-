from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started  with widgets")
root.geometry("400x300")

lb = Label(text="Hey,There!", fg="white", bg="#072F5F", height = 5, width = 300)
name_lbl = Label(text="Full name", bg="#3895D3", fg="red")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())


text_box = Text(height=5)

btn = Button(text="Begin", command=display, bg="#1261A0", fg="white")
lb.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()