from tkinter import *
class CommanderWindow:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.label = Label(master, text="Total Size: 3.4M")
        self.listbox1 = Listbox(master)
        self.listbox1.insert(1, "[..]")
        self.listbox1.insert(2, "python")
        self.listbox1.insert(3, "java")
        self.listbox1.insert(4, "html")

        self.listbox2 = Listbox(master, width=130)
        self.listbox2.insert(1, "main.js (4K)")
        self.listbox2.insert(2, "google-service.json (1K)")
        self.listbox2.insert(3, "index.html (1K)")
        self.listbox2.insert(4, "city.list.json (1.2M)")

        # layuot
        self.listbox1.grid(row=0, column=0, columnspan=3,
                          rowspan=3)
        self.listbox2.grid(row=0, column=3, columnspan=45,
                          rowspan=3)
        self.label.grid(row=4, column=0, sticky=W)


    def add(self):
        pass

root = Tk()
my_window = CommanderWindow(root )
root.geometry("300x200")
root.mainloop() # blocking

print("Goodbye...")
