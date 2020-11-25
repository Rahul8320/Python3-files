
from tkinter import *
from datetime import date
from PIL import Image, ImageTk

root = Tk()
root.title("Age Calculator")
root.geometry("900x650+120+120")

photo = ImageTk.PhotoImage(Image.open("Photo.png"))
myimage = Label(image=photo)
myimage.grid(row=0, column=1)


def calculatage():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text=f"Hey {nameValue.get()}, Your age is {age}", font="Times 20", fg="Red").grid(row=6, column=1)


Label(text="Name", font="Times 20", fg="green").grid(row=1, column=0, padx=90)
Label(text="Year", font="Times 20", fg="green").grid(row=2, column=0)
Label(text="Month", font="Times 20", fg="green").grid(row=3, column=0)
Label(text="Day", font="Times 20", fg="green").grid(row=4, column=0)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=60, bd=5, bg="sky blue")
yearEntry = Entry(root, textvariable=yearValue, width=60, bd=5, bg="sky blue")
monthEntry = Entry(root, textvariable=monthValue, width=60, bd=5, bg="sky blue")
dayEntry = Entry(root, textvariable=dayValue, width=60, bd=5, bg="sky blue")

nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)


Button(text="Calculate Age", font="bold", fg="blue", bg="pink", command=calculatage).grid(row=5, column=1, pady=10)
Button(text="Exit Program", font="bold", fg="blue", bg="pink", command=root.quit).grid(row=7, column=1, pady=10)


root.mainloop()
