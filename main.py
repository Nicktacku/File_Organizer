from tkinter import Tk
from tkinter import filedialog, Entry, Button, Label, Radiobutton, IntVar
import os
import shutil


def get_directory(dir, entry_to_update):
    # get a directory path by user
    filepath = filedialog.askdirectory(initialdir=dir, title="Dialog box")
    if entry_to_update == 1:
        dir_to_change.delete(0, "end")
        dir_to_change.insert(0, filepath)
    elif entry_to_update == 2:
        dir_to_move.delete(0, "end")
        dir_to_move.insert(0, filepath)

    return filepath


def organize_files(method, path1, path2):
    def by_keyword(keyword):
        files = os.listdir(path1)

        for file in files:
            file_name, _ = os.path.splitext(file)

            keyword_path = f"{path2}/{keyword}"
            file_path = f"{path2}/{file}"

            if keyword.lower() in file_name.lower():
                if os.path.exists(keyword_path):
                    shutil.move(file_path, keyword_path + "/" + file)
                else:
                    os.makedirs(keyword_path)
                    shutil.move(file_path, keyword_path + "/" + file)

    if method == 1:
        files = os.listdir(path1)

        for file in files:
            filename, type = os.path.splitext(file)
            type = type[1:]

            type_path = f"{path2}/{type}"
            file_path = f"{path2}/{file}"

            if os.path.exists(type_path):
                shutil.move(file_path, type_path + "/" + file)
            else:
                os.makedirs(type_path)
                shutil.move(file_path, type_path + "/" + file)

    elif method == 2:
        for widgets in root.winfo_children():
            widgets.destroy()
        keyword_label = Label(root, text="Enter Keyword")
        keyword_label.pack()
        keyword = Entry(root)
        keyword.pack()

        confirm_btn = Button(
            root, text="Confirm", command=lambda: by_keyword(keyword.get())
        )
        confirm_btn.pack()


root = Tk()
root.geometry("400x400")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

current_label = Label(root, text="Choose directory to organize")
current_label.pack()

dir = r"C://"

dir_to_change = Entry(root)
dir_to_change.insert(0, dir)
dir_to_change.pack()

current_btn = Button(
    root, text="change directory", command=lambda: get_directory(dir, 1)
)
current_btn.pack()

new_dir_label = Label(root, text="Choose directory to move the organized files")
new_dir_label.pack()

dir = r"C://"

dir_to_move = Entry(root)
dir_to_move.insert(0, dir)
dir_to_move.pack()

new_dir_btn = Button(
    root, text="change directory", command=lambda: get_directory(dir, 2)
)
new_dir_btn.pack()

method_label = Label(root, text="Choose method to organize files")
method_label.pack()

method = IntVar(None, 1)

c1 = Radiobutton(root, text="By Type", value=1, variable=method)
c2 = Radiobutton(root, text="By Keyword", value=2, variable=method)
c1.pack()
c2.pack()

organize = Button(
    root,
    text="Start Organizing",
    command=lambda: organize_files(
        method.get(), dir_to_change.get(), dir_to_move.get()
    ),
)
organize.pack()

root.mainloop()
