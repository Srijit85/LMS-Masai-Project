# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 01:31:21 2025

@author: Ateesh
"""

# Step 1: Setup the board
def initialize_board():
    return [" " for _ in range(9)]  # Created a list with 9 spaces

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Step 2: Check if someone has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Step 3: Check if the board is full (to check for a tie)
def is_board_full(board):
    return " " not in board

# Step 4: Get Player Move
def get_player_move(board):
    while True:
        try:
            move = int(input(f"Enter a position (0-8): "))
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move! The spot is already taken or out of range. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")

# Step 5: Main Game Loop
def play_game():
    board = initialize_board()
    current_player = "X"
    
    for turn in range(9):  # 9 turns max, since there are 9 spots on the board
        print_board(board)
        print(f"Player {current_player}'s turn:")
        move = get_player_move(board)
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Step 6: Starting the Game
if __name__ == "__main__":
    play_game()
