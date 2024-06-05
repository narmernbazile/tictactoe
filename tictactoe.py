# tictactoe.py: a simple program that allows for a tic tac toe game to be played
# between two players.

import os
import time

# print_board() is a method that constructs a string representing the tic tac
# toe board and prints it to the console.
# It takes the tic tac toe board as an argument.
def print_board(board):
    print("     0       1       2   ")
    print("" + "0    " + str(board[0][0]) + "   |" + "   " + str(board[0][1]) + "   |" + "   " + str(board[0][2]))
    print("  -------|-------|-------")
    print("" + "1    " + str(board[1][0]) + "   |" + "   " + str(board[1][1]) + "   |" + "   " + str(board[1][2]))
    print("  -------|-------|-------")
    print("" + "2    " + str(board[2][0]) + "   |" + "   " + str(board[2][1]) + "   |" + "   " + str(board[2][2]))
    print()

# parse_coordinates() is a wrapper around Python's input function designed to
# parse coordinates in the form "X,Y" so they make be used to mark the tic tac toe
# board. It returns a list containing [X,Y].
def parse_coordinates(prompt_string):
    player_mark = input(prompt_string)
    x = player_mark[0]
    y = player_mark[2]
    return [int(x),int(y)]

# mark_board() if a function that assigns the mark X for Player 1 or O for Player 2
# to a specific place on the tic tac toe baord. It makes use of parse_coordinates()
# to prompt the user(s) for input before marking the releveant position.
# Returns 0 indicating sucess and -1 indicating failure.
def mark_board(player_string, board):
    if player_string == "Player1":
        mark = parse_coordinates("Player 1: ")
        board[mark[0]][mark[1]] = "X"
        return 0
    elif player_string == "Player2":
        mark = parse_coordinates("Player 2: ")
        board[mark[0]][mark[1]] = "O"
        return 0
    else:
        return -1

# is_won() returns a boolean representing whether the game has been won or not,
# with True representing the win condition, and False representing the not won
# condition.
def is_won(board):
    return test_board(board, "Player1") or test_board(board, "Player2")

# is_draw() returns a boolean representing whether the game is a draw or not,
# with True representing the draw condition, and False representing the not draw
# condition.
def is_draw(board):
    # assume that every square has been marked
    all_marked = True
    # iterate through every square
    for i in range(len(board)):
        for j in range(len(board[i])):
            # if a square is marked something other than X or O, not every square has been marked
            if not(board[i][j] == "X" or board[i][j] == "O"):
                all_marked = False
    # game is a draw if every square has been marked without meeting the win condition
    return (not is_won(board)) and all_marked

# get_board_state() is a function that returns the current state of the board.
# If the string "Player1" is returned, Player 1 has won. If the string "Player2"
# is returned, Player 2 has won. If the string "Draw" is returned, the game is a
# draw.
def get_board_state(board):
    if(test_board(board, "Player1")):
        return "Player1"
    elif(test_board(baord, "Player2")):
        return "Player2"
    elif(is_draw(board)):
        return "Draw"

# test_board() is a function that tests the tic tac toe board to see if a
# particular player has won. It does so by testing every possible winning tic tac toe
# position(see comments below). It takes the arguments 'board', representing the Tic
# tac toe board, and 'player_string' representing the Player that you wish to test for.
def test_board(board, player_string):
    # Player 1 has mark X, while Player 2 has mark O
    if player_string == "Player1":
        mark = "X"
    elif player_string == "Player2":
        mark = "O"
    # Error case
    else:
        return None

    # X | X | X
    # - | - | -
    # - | - | -
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True

    # - | - | -
    # X | X | X
    # - | - | -
    elif board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True

    # - | - | -
    # - | - | -
    # X | X | X
    elif board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True

    # X | - | -
    # X | - | -
    # X | - | -
    elif board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True

    # - | X | -
    # - | X | -
    # - | X | -
    elif board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True

    # - | - | X
    # - | - | X
    # - | - | X
    elif board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True

    # X | - | -
    # - | X | -
    # - | - | X
    elif board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True

    # - | - | X
    # - | X | -
    # X | - | -
    elif board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    else:
        return False

# print welcome message and information
print("Welcome to Tic Tac Toe.")
print("Player 1 will use mark \'X\'.")
print("Player 2 will use mark \'O\'.")
print("Enter the (row, column) coordinates for the square that you wish to mark.")
input("Press enter to continue.")

# the is the tic tac toe board. It is represented as a 3x3 2 dimensional list,
# with each value initialized to the string "-"
board = [
         ["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

while True:
    # present empty board to user(s)
    os.system("clear")
    print_board(board)

    # Player 1's turn
    mark_board("Player1", board)
    # Update the board
    os.system("clear")
    print_board(board)

    # If Player 1 was the last to mark before the win condition was met, then
    # he is the winner
    if is_won(board):
        print("PLAYER 1 is the winner!")
        break

    # End the game in case of a draw
    if is_draw(board):
        print("DRAW.")
        break

    # Player 2's turn
    mark_board("Player2", board)
    # Update the board
    os.system("clear")
    print_board(board)

    # If Player 2 was the last to mark before the win condition was met, then
    # he is the winner
    if is_won(board):
        print("PLAYER 2 is the winner!")
        break
    # End the game in case of a draw
    if is_draw(board):
        print("DRAW.")
        break
