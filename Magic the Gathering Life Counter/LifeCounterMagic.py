# -----------------------------------------
# LifeCounterMagic
# Author: Lauren Ryman
# Date: 4/12/2025
# Description: [Enter description here]
# -----------------------------------------
# Name: Lauren Ryman
# Course: COSC 1336
# Program: Magic: The Gathering Life Counter
# Description: This program simulates a simple 2-player life counter for Magic: The Gathering.
#              Each player starts with a default of 20 life points.
#              Players can increase or decrease their life total, and the program displays updates.
#              Includes exception handling and allows for repeated games.

DEFAULT_LIFE = 20
PLAYER_COUNT = 7
VALID_ACTIONS = ['add', 'subtract', 'show', 'exit']

def get_valid_input(prompt):
    """Ask user for a valid integer and handle ValueError."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Please enter a whole number.')

def update_life(player_lives, player_number):
    """Update the selected player's life total."""
    action = input(f"Do you want to add, subtract, show, or exit? ").strip().lower()

    if action not in VALID_ACTIONS:
        print('Please enter a valid action.')
        return True

    if action == "exit":
        return False

    if action == "show":
        print_lives(player_lives)
        return True

    amount = get_valid_input(f"How many lives would you like to {action}? ")

    if action == "add":
        player_lives[player_number] += amount
    elif action == "subtract":
        player_lives[player_number] -= amount

    print_lives(player_lives)
    return True

def print_lives(player_lives):
    """Prints the current life totals for both players."""
    print("\nCurrent Life Totals:")
    for i, life in enumerate(player_lives, start=1):
        print(f"   Player {i}: {life:>3} life")
    print("-" * 30)

def play_game():
    """Runs a full session of the life counter."""
    try:
        player_lives = [DEFAULT_LIFE] * PLAYER_COUNT
        print("\nMAGIC: THE GATHERING LIFE COUNTER")
        print_lives(player_lives)

        continue_game = True
        while continue_game:
            player = get_valid_input("Which player would you like to update? (1 or 2): ") - 1
            if player not in [0, 1]:
                print("Please enter a valid player number.")
                continue
            continue_game = update_life(player_lives, player)

    except Exception as e:
        print("An error occurred:", e)

def main():
    """Main loop to allow multiple games."""
    while True:
        play_game()
        answer = input("Would you like to play again? (y/n): ").strip().lower()
        if answer != 'y':
            print("Thanks for playing! Bye!")
            break

# Run the program
if __name__ == "__main__":
    main()