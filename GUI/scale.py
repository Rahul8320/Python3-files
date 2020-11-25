# scale in tkinter
from tkinter import *

class Scale_class:

    def select(self):
        sel = "Value = " + str(self.v.get())
        self.label.config(text=sel)

    def __init__(self, master):
        self.master = master
        master.geometry("300x200+120+120")
        master.title("Scale")

        self.v = DoubleVar
        self.scale = Scale(self.master, variable=self.v, from_=1, to=50, orient=HORIZONTAL)
        self.scale.pack(anchor=CENTER)

        self.btn = Button(self.master, text="Value", command=self.select)
        self.btn.pack(anchor=CENTER)

        self.label = Label(self.master)
        self.label.pack()


root = Tk()

sc = Scale_class(root)

root.mainloop()