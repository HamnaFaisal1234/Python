from tkinter import *
window = Tk()
window.title("Sample window ")
window.geometry("200x200")

greeting =Label(text = "Hi welcome", fg = "red", bg = "yellow", height=10, width=100)

greeting.pack()
frame = Frame(master=window,relief = RAISED , borderwidth = 5 )
frame.pack()
label = Label (master= frame , text="sample")
label.pack()
button =Button(text = "Click here", fg = "white", bg = "black", height=3, width=30)
button.pack()
textbox = Text(bg="blue" , fg="white" , height=7, width=50)
textbox.pack()
window.mainloop()


