# Assignment: Tic-tac-toe
# Author: David Sowa

# Series of functions that provide necessary services to the ticTacToe.py file.

# Draws the game board
def draw_board(squares):
    board = (f"\033[0;49;37m{squares[1]} | {squares[2]} | {squares[3]}\n"
             f"- + - + -\n"
             f"{squares[4]} | {squares[5]} | {squares[6]}\n"
             f"- + - + -\n"
             f"{squares[7]} | {squares[8]} | {squares[9]}\n")
    print(board)

# Verifies whose turn it is
def verify_turn(turn):
    if turn % 2 == 0: return '\033[0;49;31m0\033[0;49;37m'
    else: return '\033[0;49;32mX\033[0;49;37m'

# Determines if someone has won
def victory_conditions(squares):

    # if horizontal lines match then victory
    if   (squares[1] == squares[2] == squares[3]) \
      or (squares[4] == squares[5] == squares[6]) \
      or (squares[7] == squares[8] == squares[9]):
      return True

    # if vertical lines match then victory
    elif   (squares[1] == squares[4] == squares[7]) \
      or   (squares[2] == squares[5] == squares[8]) \
      or   (squares[3] == squares[6] == squares[9]):
      return True

    # if transversal lines match then victory
    elif   (squares[1] == squares[5] == squares[9]) \
      or   (squares[3] == squares[5] == squares[7]):
      return True
    
    # if none of the above no victory
    else: return False