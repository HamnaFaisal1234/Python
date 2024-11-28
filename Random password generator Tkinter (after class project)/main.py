import tkinter as tk
import random
import string


def generate_password():
    
    length = int(entry.get())
    characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    
    
    password_display.delete(0, tk.END)  
    password_display.insert(0, password)


window = tk.Tk()
window.title("Simple Password Generator")


label = tk.Label(window, text="Enter password length:")
label.pack()


entry = tk.Entry(window)
entry.pack()


button = tk.Button(window, text="Generate Password", command=generate_password)
button.pack()


password_display = tk.Entry(window)
password_display.pack()


window.mainloop()
