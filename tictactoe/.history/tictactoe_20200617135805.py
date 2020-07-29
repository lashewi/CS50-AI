"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    xcounter = 0
    ocounter = 0

    for row in board:
        xcounter += row.count(X)
        ocounter += row.count(O)

    return X if xcounter <= ocounter else O


def actions(board):

    possible_moves = set()

    for i, row in enumerate(board):
            for j, space in enumerate(row):
                    possible_moves.add((i, j))

    return possible_moves


def result(board, action):

    i, j = action
    new_board = Copy.deepcopy(board)
    current_player = player(new_board)

    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid action.")
    else:
        new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
