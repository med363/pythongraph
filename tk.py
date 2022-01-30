from tkinter import *
from tkinter import ttk


# declare title , size et type d'input tkinter
root = Tk()
root.title("spannig tree")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Test SariSari Store"




def bb():
    test=entry.get()
    print(test)
    return None

entry= Entry(root,width=20)
entry.pack()

Button(root, text="button",command=bb).pack()




root.mainloop()

