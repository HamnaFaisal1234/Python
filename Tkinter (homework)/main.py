from tkinter import *
window = Tk()
window.title("Button")
window.geometry("500x500")


frame = Frame(window, bg="black", height=650, width=480)
frame.pack_propagate(False) 
frame.pack(pady=50)  


greeting = Label(frame, text="Hey👋🏻\nI am Hamna, and I want to show you a button which I have created." , fg="white", bg="black", wraplength=400,font=("Arial", 14))
greeting.pack(pady=20)  


button = Button(frame, text="Click me", bg="white", fg="black",bd=5,font=("Arial", 14, "bold"),relief="groove")
button.pack(pady=10)
def on_enter(e):
    button.config(bg="blue", fg="white") 

def on_leave(e):
    button.config(bg="white", fg="black")  

button.bind("<Enter>", on_enter)  
button.bind("<Leave>", on_leave)

window.mainloop()