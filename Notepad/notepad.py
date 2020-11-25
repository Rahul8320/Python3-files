
from tkinter import *
from tkinter import filedialog


class Textpad:
    current_open_file = "no file"

    # declaration of open_file function--->
    def open_file(self):
        open_return = filedialog.askopenfile(initialdir="C:\\Users\\Windows 10\\Desktop", title="select to open file", filetypes=(("text files", "*.txt"),("all files", "*.*")))
        if open_return != None:
            self.text_area.delete(1.0, END)
            for line in open_return:
                self.text_area.insert(END, line)
            self.current_open_file = open_return.name
            open_return.close()

    # declaration of save_as_file function--->
    def save_as_file(self):
        f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        text2save = self.text_area.get(1.0, END)
        self.current_open_file = f.name
        f.write(text2save)
        f.close()

    # declaration of save_file function--->
    def save_file(self):
        if self.current_open_file == "no file":
            self.save_as_file()
        else:
            f = open(self.current_open_file, "w+")
            f.write(self.text_area.get(1.0, END))
            f.close()

    # declaration of new_file function--->
    def new_file(self):
        self.text_area.delete(1.0, END)
        self.current_open_file = "no file"

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first", "sel.last")

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste_text(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())

    def __init__(self, master):
        self.master = master
        master.title("TextPad")                                                  # set the title name
        master.iconbitmap(r"notepad.ico")                                        # set the logo

        # creating the text area ---->
        self.text_area = Text(self.master, undo=True)
        self.text_area.pack(fill=BOTH, expand=1)

        # creating main menu ---->
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)

        # creating file menu ---->
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)            # function in line no 39.
        self.file_menu.add_command(label="Open", command=self.open_file)          # function in line no 10.
        self.file_menu.add_separator()                                            # create a line in file_menu
        self.file_menu.add_command(label="Save", command=self.save_file)          # function in line no 30.
        self.file_menu.add_command(label="Save as", command=self.save_as_file)    # function in line no 20.
        self.file_menu.add_separator()                                            # create a line in file_menu
        self.file_menu.add_command(label="Exit", command=master.destroy)          # self function.

        # creating edit menu ---->
        self.edit_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)  # self function
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)  # self function
        self.edit_menu.add_separator()                                              # create line in edit_menu
        self.edit_menu.add_command(label="Cut", command=self.cut_text)              # function in line no 43.
        self.edit_menu.add_command(label="Copy", command=self.copy_text)            # function in line no 47.
        self.edit_menu.add_command(label="Paste", command=self.paste_text)          # function in line no 51.


root = Tk()

te = Textpad(root)

root.mainloop()
