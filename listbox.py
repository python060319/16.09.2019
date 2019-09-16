from tkinter import *

top = Tk()
top.title("File system project")
top.geometry("200x250")

lbl = Label(top, text="A list of favourite countries...")

listbox = Listbox(top)

listbox.insert(1, "India")

listbox.insert(2, "USA")

listbox.insert(3, "Japan")

listbox.insert(4, "Austrelia")

# this button will delete the selected item from the list

def printit():
    print(listbox.get(0, "end")[listbox.curselection()[0]])

btn = Button(top, text="delete", command=printit)


def dbl(item):
    print(listbox.curselection()[0])
listbox.bind('<Double-Button>', dbl)

lbl.pack()

listbox.pack()

btn.pack()
top.mainloop()
