import tkinter as tk


window = tk.Tk()

window.title("first window")

window.geometry("800x600")

def my_func():
    pass

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)
editmenu = tk.Menu(menubar,tearoff=0)


menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=my_func)
filemenu.add_command(label="Open",command=my_func)
filemenu.add_command(label="Save",command=my_func)
filemenu.add_command(label="Exit",command=window.quit)


menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo",command=my_func)
editmenu.add_command(label="Redo",command=my_func)
editmenu.add_command(label="Copy",command=my_func)
editmenu.add_command(label="Cut",command=my_func)



window.config(menu=menubar)

window.mainloop()