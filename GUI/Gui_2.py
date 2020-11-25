
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x600+150+150")
root.title("Frame")

mylab1 = Label(root, text="Welcome", bg="red", fg="white")
mylab = Label(root, text="Hey User!!!", bg="blue", fg="white")
mylab2 = Label(root, text="press bellow to exit!!!", bg="green", fg="white")

mylab.pack(fill=X)
mylab1.pack(fill=X)
mylab2.pack(side=LEFT, fill=Y)


frame = Frame(root, width=300, height=300, bd=5)
img = ImageTk.PhotoImage(Image.open("C://Users//Windows 10//Desktop//Web-Py//File//Images//BMW 1.jpg"))
imglab = Label(frame, image=img, width=500, height=500)
imglab.pack(side=TOP)
frame.pack()


b = Button(root, text="Exit Program", command=root.quit, bg="yellow", fg="red")
b.pack(side=BOTTOM, fill=X)


root.mainloop()
