
from tkinter import *

root = Tk()

root.geometry("400x300")

root.title("main")

def topwin():

  top = Toplevel()

  top.geometry("180x100")

  top.title("toplevel")

  l2 = Label(top, text = "I am Hamna")

  l2.pack()

  top.mainloop()

l = Label(root, text = "This is root window")

btn = Button(root, text = "Click here then I will tell you what is my name", command = topwin)

l.pack()

btn.pack()
root.mainloop()