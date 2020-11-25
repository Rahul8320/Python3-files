from tkinter import *

root = Tk()
root.geometry("700x500+150+150")
root.title("Khepa")

frame = LabelFrame(root, text="My Frame", width=700, height=500, bd=5, bg="sky blue", fg="red")

label1 = Label(frame, text="Hello user !!", padx=10, pady=10, fg="blue", bg="pink")
label2 = Label(frame, text="Welcome to GUI APPLICATION !!", padx=10, pady=10, fg="blue", bg="pink")
label3 = Label(frame, text="Want To Exit ,Click Bellow !!", padx=10, pady=10, fg="blue", bg="pink")


label1.grid(row=0, column=0, padx=20, pady=20)
label2.grid(row=1, column=0, padx=20, pady=20)
label3.grid(row=2, column=0, padx=20, pady=20)


def left(event):
    print("U r clicked left button.")


def middle(event):
    print("U r clicked middle button.")


def right(event):
    print("U r clicked right button.")


button = Button(frame, text="click me", bg="blue")
button.bind("<Button-1>", left)
button.bind("<Button-2>", middle)
button.bind("<Button-3>", right)


button.grid(columnspan=2)


frame.grid(row=0, column=0, padx=30, pady=30)

button = Button(root, text="Exit Program", padx=10, pady=10, command=root.quit, bg="orange", fg="green")
button.grid(row=1, column=0, pady=20)

root.mainloop()
