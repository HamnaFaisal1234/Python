from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("400x300")
root.title("Age to Birth Year Calculator")

def calculate_birthday():
    
        current_year = datetime.now().year
        
        age = int(age_entry.get())
        
        birth_year = current_year - age
        
        result_label.config(text=f"Your birth year is: {birth_year}")
    

input = Label(root, text="Enter your age:")
input.pack()

age_entry = Entry(root)
age_entry.pack()


calculate_button = Button(root, text="Calculate Birth Year", command=calculate_birthday)
calculate_button.pack()


result_label = Label(root, text="")
result_label.pack()


root.mainloop()
