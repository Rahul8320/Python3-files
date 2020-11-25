from tkinter import messagebox
from tkinter import *

root = Tk()
root.geometry("800x600+150+100")
root.title("GUI Menu")
root["bg"] = "black"

global var
var = []


def save_file():
    messagebox.showinfo("Success", "File Saved")


def new():
    frame = Frame(root, width=700, height=500, bd=5, bg="sky blue", padx=15, pady=20)
    frame.pack(padx=100, pady=50)

    def close():
        frame.forget()

    def save():
        global var
        k = e.get()
        var.append(k)

    e = Entry(frame, width=50, borderwidth=7)
    e.pack(side=TOP, fill=X)

    b2 = Button(frame, text="save", command=save, bg="red", fg="white")
    b2.pack(padx=10, pady=10)

    b = Button(frame, text="Exit Window", command=close, bg="red", fg="white")
    b.pack(side=BOTTOM)


def open_file():
    frame = Frame(root, width=600, height=400, bd=5, bg="sky blue", padx=15, pady=20)
    frame.pack(padx=100, pady=50)

    def close():
        frame.forget()

    def show():
        global var
        label = Label(frame, text=var)
        label.pack(padx=10, pady=10)

    b2 = Button(frame, text="Show", command=show, bg="pink", fg="black")
    b2.pack(side=TOP, pady=5, fill=X)

    b = Button(frame, text="Exit Window", command=close, bg="red", fg="white")
    b.pack(side=BOTTOM)


def exit_file():
    ans = messagebox.askquestion("exit", "Do u want to really exit ?")
    if ans == 'yes':
        root.quit()


main_menu = Menu(root)
root.config(menu=main_menu)

# creating file menu
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)

# creating edit menu
edit_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit", menu=edit_menu)

file_menu.add_command(label="New", command=new)
file_menu.add_command(label="New Folder", command=new)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_file)


def nothing():
    print("Working..")


edit_menu.add_command(label="Cut", command=nothing)
edit_menu.add_command(label="Past", command=nothing)

find_menu = Menu(edit_menu)
find_menu.add_command(label="Find Word", command=nothing)
find_menu.add_command(label="Find Path", command=nothing)
find_menu.add_command(label="Find Directory", command=nothing)


edit_menu.add_cascade(label="Find", menu=find_menu)


root.mainloop()
