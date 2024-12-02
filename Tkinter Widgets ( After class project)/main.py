from tkinter import *
import random

def determine_winner(player_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    player_label.config(text=f"Player: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)


main = Tk()
main.title("Game")
main.geometry("500x400")
main.config(bg="lightblue")

Lab = Label(main, text="Enjoy your *** Free *** Game", font=("bold", 20), bg="red", fg="white")
Lab.pack(ipadx=100, ipady=20, fill="x")


player_label = Label(main, text="Player: None", font=("Arial", 12), bg="lightblue")
player_label.pack()

computer_label = Label(main, text="Computer: None", font=("Arial", 12), bg="lightblue")
computer_label.pack()


result_label = Label(main, text="", font=("Arial", 14), bg="lightblue", fg="green")
result_label.pack(pady=20)


button_frame = Frame(main, bg="lightblue")
button_frame.pack()

rock_button = Button(button_frame, text="Rock", height=2, width=10, command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = Button(button_frame, text="Paper", height=2, width=10, command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = Button(button_frame, text="Scissors", height=2, width=10, command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)


quit_button = Button(main, text="Quit", height=2, width=15, bg="red", fg="white", command=main.quit)
quit_button.pack(pady=30)

main.mainloop()
