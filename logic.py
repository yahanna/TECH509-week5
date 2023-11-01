# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def get_winner(board):
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]

        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
   
def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    else:
        return 'X'
