#from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E
from tkinter import *
'''
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI for python powerpoint creation")

        self.label = Label(master, text="Please input your file location :)")
        self.label.pack()

        self.label_text = StringVar()
        self.label = Label(master, textvariable=self.label_text)    
        
        self.greet_button = Button(master, text="Click here once entered", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        
    def greet(self):
        print("Greetings!")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
'''
"""
class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
"""

colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1
mainloop()
