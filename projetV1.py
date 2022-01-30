# import tkinter as tk
import os
import time
from tkinter import *
from tkinter import ttk
import tkinter as tk


# declare title , size et type d'input tkinter
root = Tk()
root.title("spannig tree")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Test SariSari Store"


# def which_button(button_press):
#        print (button_press)


def remplir():
    l1=[]
    l2=[]
    l3=[]
    while 1:
        n1=str(entrySwitch.get())
        print(n1)
        if n1=="":
            break
        l1.append(n1)
        if buttonOUI['state'
        
            
        n2=str(entryVoisin.get())
        print(n2)
        if n2=="":
            break
        elif n2 not in l3:
            l2.append(n2)
            print("donnez la valuer de ",n1, "vers ", n2)
            val=int(entryCout.get())
            print(val)
            l3.append(val)
        arcs=list(zip(l1,l2,l3))
    print(arcs)









# label of input
switchLabel = Label(root, text="switch", font=('Arial bold', 15))
QuestionLabel=Label(root,text='Est que il avait un voisin?',font=('Arial bold', 15))
voisinLabel = Label(root, text="voisin", font=('Arial bold', 15))
coutLabel = Label(root, text="cout", font=('Arial bold', 15))
switchLabel.grid(row=1, column=0, padx=10, pady=10)
QuestionLabel.grid(row=2, column=0, padx=10, pady=10)
voisinLabel.grid(row=4, column=0, padx=10, pady=10)
coutLabel.grid(row=5, column=0, padx=10, pady=10)
# type of input
entrySwitch = Entry(root, width=25, bd=5, font=('Arial bold', 15))
# entrySwitch.pack()
entryVoisin = Entry(root, width=25, bd=5, font=('Arial bold', 15))
# entryVoisin.pack()
entryCout = Entry(root, width=25, bd=5, font=('Arial bold', 15))
# entryCout.pack()
entrySwitch.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
entryVoisin.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
entryCout.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
# buttom of question
# def switchButtonState():
#     if (buttonNON['state'] == tk.NORMAL):
#         buttonNON['state'] = tk.DISABLED
#     else:
#         buttonNON['state'] = tk.NORMAL
buttonOUI = Button(
    root, text="Oui", padx=5, pady=5, width=10,
    bd=3, font=('Arial', 15), bg="#0099ff")
buttonOUI.grid(row=3, column=0, columnspan=1)
buttonNON = Button(
    root, text="Non", padx=5, pady=5, width=10,
    bd=3, font=('Arial', 15), bg="#e62e00", )
buttonNON.grid(row=3, column=1, columnspan=1)
# buttonOUI = tk.Button(root, text="Python Button 1",
#                     state=tk.DISABLED)
# buttonNON = tk.Button(root, text="EN/DISABLE Button 1",
#                     command = switchButtonState)
# buttonOUI.pack(side=tk.LEFT)
# buttonNON.pack(side=tk.RIGHT)
# buttom remplir
buttonEnter = Button(
    root, text="remplir la topologie", padx=5, pady=5, width=30,
    bd=3, font=('Arial', 15), bg="#0099ff",command=remplir)
buttonEnter.grid(row=6, column=0, columnspan=1)
# button update
# buttonUpdate = Button(
#     root, text="Update", padx=5, pady=5, width=5,
#     bd=3, font=('Arial', 15), bg="#ffff00", command=)
# buttonUpdate.grid(row=5, column=2, columnspan=1)
# button delete
buttonDelete = Button(
    root, text="supprimer un commutateur", padx=5, pady=5, width=30,
    bd=3, font=('Arial', 15), bg="#e62e00")
buttonDelete.grid(row=6, column=1, columnspan=1)

   

root.mainloop()