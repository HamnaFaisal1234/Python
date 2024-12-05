from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Main window setup
window = Tk()
window.title("Domination calculator")
window.geometry("600x500")
window.configure(bg="light blue")

# Load and display image
upload = Image.open("fhej.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(window, image=image, bg="blue")
label.place(x=300, y=150, anchor=CENTER)  # Adjusted placement for visibility

label1 = Label(window, text="Hey👋🏻, You are here to use Domination calculator", bg="light blue")
label1.place(relx=0.5, y=400, anchor=CENTER)


def topwin():
    # Create a new window
    top = Toplevel()
    top.title("Domination calculator")
    top.geometry("600x400")
    top.configure(bg="light grey")

    # Define widgets inside topwin
    label = Label(top, text="Enter total amount:", bg="light grey", font=("Arial", 12))
    label.pack(pady=10)

    entry = Entry(top, width=20, font=("Arial", 12))
    entry.pack(pady=5)

    lbl = Label(top, text="Number of notes for each denomination:", bg="light grey", font=("Arial", 12))
    lbl.pack(pady=10)

    # Labels for note denominations
    l1 = Label(top, text="2000:", bg="light grey", font=("Arial", 12))
    l2 = Label(top, text="500:", bg="light grey", font=("Arial", 12))
    l3 = Label(top, text="100:", bg="light grey", font=("Arial", 12))

    # Entry fields for results
    t1 = Entry(top, width=10, font=("Arial", 12))
    t2 = Entry(top, width=10, font=("Arial", 12))
    t3 = Entry(top, width=10, font=("Arial", 12))

    # Place labels and entry fields using grid
    l1.place(x=150, y=150)
    t1.place(x=250, y=150)

    l2.place(x=150, y=200)
    t2.place(x=250, y=200)

    l3.place(x=150, y=250)
    t3.place(x=250, y=250)

    # Calculator function to handle calculations
    def calculator():
        try:
            # Fetch input and calculate note counts
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            # Display results
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    # Add Calculate button
    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white", font=("Arial", 12))
    btn.place(x=220, y=300)


# Show confirmation message and open new window
def msg():
    MsgBox = messagebox.askyesno("Alert", "Do you want to calculate the Domination count?")
    if MsgBox:  # If user clicks 'Yes'
        topwin()


# Button to start the calculator
button = Button(window, text="Let's start", command=msg, font=("Arial", 12))
button.place(relx=0.5, y=450, anchor=CENTER)

# Run the main loop
window.mainloop()
