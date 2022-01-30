# import tkinter

# class App(object):
#     def __init__(self):
#         self.tree = None
#         self._setup_widgets()

#     def _setup_widgets(self):
#         butts = tkinter.Button(text = "add line", state="disabled")
#         butts.grid()

# def main():  
#     root = tkinter.Tk()
#     app = App()
#     root.mainloop()

# if __name__ == "__main__":
#     main()


# import tkinter as tk
    

# app = tk.Tk()
# app.geometry("300x100")
# button1 = tk.Button(app, text="Button 1",
#                     state=tk.DISABLED)
# button2 = tk.Button(app, text="EN/DISABLE Button 1")
# button1.pack(side=tk.LEFT)
# button2.pack(side=tk.RIGHT)
# app.mainloop()

# importing tkinter module
# along with some constants and Widgets
from tkinter import Tk
from tkinter.constants import DISABLED, NORMAL
from tkinter.ttk import Button, Label
  
# Creating App class
# which will contain our overall App
class App:
    def __init__(self, master) -> None:
  
        # Instantiating master 
        # i.e toplevel Widget
        self.master = master
  
        # Creating label
        self.label = Label(self.master,
                           text="Click Button2 to change Button1 State")
          
        self.label.pack(pady = 10)
  
        # Creating button1
        # We will change the state of this Button
        # it has a initial state of 
        # "NORMAL" i.e Button can be pressed
        self.button1 = Button(self.master, 
                              text = "Button1", 
                              state = NORMAL)
          
        self.button1.pack(pady = 20)
  
        # Creating another button
        # We will use this button
        # to change the State of first button
        self.button2 = Button(self.master,
                              text = "Button2",
                              command = self.changeState)
          
        self.button2.pack(pady = 20)
  
    # Helper function which will 
    # change the State of Button1
    def changeState(self) -> None:
  
        # Printing the State of 
        # the Button before ALTERING it
        # This is optional
        print(self.button1['state'])
  
        # Checking if the STATE of the Button1
        # If the STATE is NORMAL
        if (self.button1['state'] == NORMAL):
  
            # Change the state to DISABLED
            self.button1['state'] = DISABLED
        else:
  
            # Otherwise, change the state to NORMAL
            self.button1['state'] = NORMAL
  
  
if __name__ == "__main__":
  
    # Instantiating top level
    root = Tk()
  
    # Setting the title of the window
    root.title("Button State App")
  
    # Setting the geometry i.e Dimensions
    root.geometry("400x250")
  
    # Calling our App
    app = App(root)
  
    # Mainloop which will cause this toplevel
    # to run infinitely
    root.mainloop()