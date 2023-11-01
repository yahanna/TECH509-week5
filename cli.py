# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board,get_winner,other_player

# Reminder to check all the tests

def print_board(board):
    for i in range(3):
        row_str = " | ".join(cell if cell is not None else ' ' for cell in board[i])
        print(row_str)
        if i < 2:
            print("---------")

def is_board_full(board):
    return all(cell is not None for row in board for cell in row)

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'

    while winner is None and not is_board_full(board):
        print(f"Current board:")
        print_board(board)

        print(f"Player {player}'s turn.")
        row = int(input("Enter the row (0, 1, or 2): "))-1
        col = int(input("Enter the column (0, 1, or 2): "))-1

        if board[row][col] is None:
            board[row][col] = player
            winner = get_winner(board)
            player = other_player(player)
        else:
            print("Invalid move. That cell is already occupied.")

    print(f"Final board:")
    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie! Nobody wins.")
