# Assignment: Tic-tac-toe
# Author: David Sowa
# 
# .............................................................................
# | * IMPORTS *                                                               |
# |_______________________________________________________________________    | 
# | Gets necessary functions from the supporting ticTacToeFunctions file. |   |
# \-----------------------------------------------------------------------/   |      
from ticTacToeFunctions import draw_board, verify_turn, victory_conditions
#  _________________________________________________________________________   
# | Imports python operating system functions so python can detect which os | |
# | it is running on then provide it the approriate commands to clear the   | |
# | output by replacing it with a new output.                               | |
# \-------------------------------------------------------------------------/ |
import os
# .............................................................................

#   <<<<>>>>>
#   * START *
#   <<<<>>>>>

def main():
    # Dictionary to keep assign and hold values for the squares of the board
    squares = {1 : '1',
               2 : '2',
               3 : '3',
               4 : '4',
               5 : '5',
               6 : '6',
               7 : '7',
               8 : '8',
               9 : '9',}

    # Variables for loop
    still_playing = True
    victory = False
    tie = False
    turn = 0
    previous_turn = -1

    # Loop, since games have variable lengths
    while still_playing:

        # Clears screen in between moves
        os.system('cls' if os.name == 'nt' else 'clear')

        # Draws game board
        draw_board(squares)

        # Lets the player repeat his turn when he makes an invalid move. 
        if previous_turn == turn:
          print("\033[0;49;93mPlease choose a valid square by typing one of the numbers displayed on the board into the terminal.")
        
        # Resets the invalid turn
        previous_turn = turn

        # Clarifies who's turn it is and how to quit
        print(f"\033[0;49;37mPlayer {str((turn % 2) +1)}'s turn: Pick your square or press q to quit")

        # Stores what the player chose on his turn
        choice = input()

        # Allow players to quit
        if choice == 'q':
          still_playing = False

        # Makes sure the input is an integer from 1-9
        elif str.isdigit(choice) and int(choice) in squares:

          # Makes sure that the choices cannot overwrite each other
          if not squares[int(choice)] in {"X", "0"}:

            # If the prior conditions are satisfied, the turns proceed
            # and squares are filled in according to the player's choice
            turn += 1
            squares[int(choice)] = verify_turn(turn)

        # Determines if someone has won the game and stops the game if true
        if victory_conditions(squares): still_playing, victory = False, True 

        # If no one has won by turn 8, declares a tie and ends game
        if turn > 8: still_playing, tie = False, True
    
    # Displays the board after the game has ended, same procedure as in the loop
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(squares)

    # Displays victory, tie and generic exit messages
    if victory:
        if verify_turn(turn) == 'X' : print("\033[0;49;96mPlayer 1 has won!\033[0;49;37m")
        else: print("\033[0;49;96mPlayer 2 has won!\033[0;49;37m")
    elif tie:
        print("\033[0;49;37mTie game. Thanks for playing!")
    else:
        print("\033[0;49;37mGame successfully exited. Thanks for playing!")

if __name__ == "__main__":
    main()