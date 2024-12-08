import tkinter as tk
import random



def decide_winner(player_choice):
    choices = ["Rock",'Paper','Scissors']
    computer_choice=random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice =='Rock' and computer_choice == 'Scissors') or\
         (player_choice =='Paper' and computer_choice == 'Rock') or\
         (player_choice =='Scissors' and computer_choice == 'Paper'):
        result = "You wins!"
        global player_score
        player_score += 1
    else:
        result = 'Computer wins!'
        global computer_score
        computer_score += 1

    result_label.config(text=f"Result: {result}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    score_label.config(text=f"Score - You: {player_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock , Paper and Scissors game")

player_score = 0
computer_score=0

title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 16) ,bg="Purple")
title_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: None", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: None", font=("Arial", 12))
result_label.pack()

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: decide_winner('Rock'))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: decide_winner('Paper'))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: decide_winner('Scissors'))
scissors_button.grid(row=0, column=2, padx=5, pady=5)


root.mainloop()


    
