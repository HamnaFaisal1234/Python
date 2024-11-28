from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title("Button")
root.geometry("400x400")


def show_alert():
    messagebox.showinfo("Alert", "You clicked the button!")


upload = Image.open("muslim girl.jpg")  
image = ImageTk.PhotoImage(upload)


label = Label(root, image=image, height=700, width=300)
label.place(x=50, y=0)


label2 = Label(root, text="I am Hamna")
label2.place(x=40, y=360)


button = Button(root, text="Click me", bg="white", fg="black", bd=5, font=("Arial", 14, "bold"), relief="groove", command=show_alert)
button.place(x=150, y=320)  


root.mainloop()
