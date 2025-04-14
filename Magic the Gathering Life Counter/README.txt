LifeCounterMagic
Author: Lauren Ryman
Date: 4/12/2025

Overview
LifeCounterMagic is a simple Magic: The Gathering life counter simulator. The program maintains life totals for multiple players (up to 7, by default set in the code). Each player starts at 20 life. Users can add or subtract life from a chosen player, display all current life totals, or exit at any time.

Key Features
Default Life Total

Each player starts with DEFAULT_LIFE = 20 points.

Multi-Player Support

An array of size PLAYER_COUNT = 7 is created, though the user interface currently prompts for player 1 or 2. (You can expand or reduce this in the code by adjusting PLAYER_COUNT or editing the prompts.)

Valid Actions

add: Increase a player’s life total by a user-specified amount.

subtract: Decrease a player’s life total by a user-specified amount.

show: Display the current life total of every player.

exit: Immediately end the update phase and return to the main game loop.

Input Validation

The program uses a custom function to ensure only integers are accepted for player selection and the amount of life points to add/subtract.

If the user enters something invalid, it prints a friendly message and re-prompts.

Exception Handling

Catches general exceptions for unexpected errors, printing a message without a raw Python traceback.

Multiple Sessions

A main loop allows repeating full games. After each session, the user is prompted whether they want to play again.

Requirements
Python 3.x or higher (standard library only)

Runs on Windows, macOS, or Linux with no extra dependencies

Usage
Clone or Download

Save this script (e.g., LifeCounterMagic.py) to your local machine.

Run the Program

Open a terminal or command prompt where the file is located.

Run:

bash
Copy code
python LifeCounterMagic.py
Follow On-Screen Prompts

When asked “Which player would you like to update? (1 or 2):”, enter 1 or 2 (note: the code as written only recognizes players 1 or 2, though an array of 7 players is created).

Next, choose to “add”, “subtract”, “show”, or “exit”.

add or subtract: You’ll be asked for how many life points you want to modify.

show: Displays the current life totals for all 7 players.

exit: Returns you to the “Which player…” prompt if you press it again, or ends if you’re in the main loop’s exit path.

Press Ctrl+C at any time to interrupt the program (it catches the exception gracefully).

Play Multiple Rounds

After a session ends, you can choose to start over or exit.

Example Interaction
sql
Copy code
MAGIC: THE GATHERING LIFE COUNTER
------------------------------
Current Life Totals:
   Player 1:  20 life
   Player 2:  20 life
   Player 3:  20 life
   ...
   Player 7:  20 life
------------------------------
Which player would you like to update? (1 or 2): 1
Do you want to add, subtract, show, or exit? add
How many lives would you like to add? 3

Current Life Totals:
   Player 1:  23 life
   Player 2:  20 life
   ...
Which player would you like to update? (1 or 2): ...
...
Would you like to play again? (y/n): n
Thanks for playing! Bye!
Possible Customizations
Adjust Player Count: Change PLAYER_COUNT to match the actual number of players in your game. Update the user prompt so they can select any valid player number (not just 1 or 2).

Change Starting Life: Modify DEFAULT_LIFE if your format starts with a different life total (e.g., 40 for Commander).

Add Logging: Log every action to a file if you want to track each move.

GUI Version: Expand to a graphical interface with buttons for each player.

License
This project is provided for educational and portfolio purposes. Feel free to adapt it for your own use or modify it to suit your needs. If you share significant modifications, credit to the original author (Lauren Ryman) is appreciated.

Contact
Have questions, issues, or ideas?
Open an issue on GitHub or send a message. Enjoy your game!