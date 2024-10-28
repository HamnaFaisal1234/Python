import random 

# Game state dictionary
game_state = {
    "target_number": random.randint(1, 100),  # Random number between 1 and 100
    "attempts": 0,
    "guess_history": []  # List to store all guesses
    
} 

# Instructions for the player
print("Welcome to the Number Guessing Game!")
print("Try to guess the number (between 1 and 100).")

# Main game loop
while True:
    guess = int(input("Enter your guess: "))
    game_state["attempts"] += 1
    game_state["guess_history"].append(guess)  # Add guess to history list

    # Check if the guess is correct
    if guess == game_state["target_number"]:
        print(f"Congratulations! You've guessed the number {guess} correctly in {game_state['attempts']} attempts.")
        break
    elif guess < game_state["target_number"]:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# Display guess history
print("\nYour guess history:")
for i, past_guess in enumerate(game_state["guess_history"], start=1):
    print(f"Attempt {i}: {past_guess}")

# End of the game message
print("\nThanks for playing!")
