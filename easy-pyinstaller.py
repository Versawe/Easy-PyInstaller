from tkinter import *
import os
import subprocess

#path = "c:\\Users\\Eric\\Documents\\"
path = ""
filename = ""


def make_magic_happen():
    path = textEntry1.get()
    filename = textEntry2.get()

    errorMsg.grid_forget()
    if(path == "" or path == " " or filename == "" or filename == " "):
        error_screen()
    if(os.path.exists(path)):
        path = path + "\\" + filename + ".py"
        if(os.path.exists(path)):
            cmd = 'PyInstaller --onefile "'+path+'"'
            subprocess.call(cmd)
            success_screen()
        else:
            error_screen()
    else:
        error_screen()


def error_screen():
    title.grid_forget()
    textEntry1.grid_forget()
    title2.grid_forget()
    textEntry2.grid_forget()
    button.grid_forget()
    successMsg.grid_forget()
    backButton.grid(row=2, column=1)
    errorMsg.grid(row=1, column=1)

def back_function():
    backButton.grid_forget()
    errorMsg.grid_forget()
    successMsg.grid_forget()
    title.grid(row=1, column=1)
    textEntry1.grid(row=2,column=1)
    title2.grid(row=3, column=1)
    textEntry2.grid(row=4,column=1)
    button.grid(row=5, column=1)

def success_screen():
    title.grid_forget()
    textEntry1.grid_forget()
    title2.grid_forget()
    textEntry2.grid_forget()
    button.grid_forget()
    errorMsg.grid_forget()
    successMsg.grid(row=1, column=1)
    backButton.grid(row=2, column=1)

tk = Tk()

title = Label(tk, text="Paste path where file is located", fg="white", bg="black", font=("Arial", '25', "bold"))
title.grid(row=1, column=1)

textEntry1 = Entry(tk, width="25", fg="white", bg="red", font="Arial")
textEntry1.grid(row=2,column=1)

title2 = Label(tk, text="py file name", fg="white", bg="black", font=("Arial", '25', "bold"))
title2.grid(row=3, column=1)

textEntry2 = Entry(tk, width="25", fg="white", bg="red", font="Arial")
textEntry2.grid(row=4,column=1)

button = Button(tk, text="Create executable", command=make_magic_happen,
fg="white", bg="red", width="20", height="2", font="Arial", cursor="tcross")
button.grid(row=5, column=1)

errorMsg = Label(tk, text="There was an error\nCheck if there are empty fields\nor if the path is wrong", fg="white", bg="red", font=("Arial", '20', "bold"))
backButton = Button(tk, text="Back", command=back_function,
fg="white", bg="red", width="20", height="2", font="Arial", cursor="tcross")

successMsg = Label(tk, text="Executable Successfully Made!", fg="white", bg="red", font=("Arial", '20', "bold"))
backButton = Button(tk, text="Back", command=back_function,
fg="white", bg="red", width="20", height="2", font="Arial", cursor="tcross")

tk.title("Easy PyInstaller")
tk.grid_columnconfigure(4, minsize=10)
tk.grid_rowconfigure(4, minsize=10)
#tk.iconbitmap('')
tk.configure(bg='black')
tk.mainloop()