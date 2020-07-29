"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from random import randint

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
    new_board = deepcopy(board)
    current_player = player(new_board)

    if new_board[i][j] is not EMPTY:
        raise Exception("Not a valid action")
    else:
        new_board[i][j] = current_player

    return new_board


def winner(board):

    #Rows 
    for row in board:
        xcounter = row.count(X)
        ocounter = row.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O
    
    #Columns
    columns = []
    for i in range(len(board)):
        column = [row[i] for row in board]
        columns.append(column)

    for j in columns:
        xcounter = j.count(X)
        ocounter = j.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O

    #Diag | Todo: Add better sol
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    # None | Todo: Modify to simplify terminal
    return None

def terminal(board):

    if winner(board) is not None:
        return True
    else:
        for row in board:
            if EMPTY in row:
                return False
        return True


def utility(board):

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board, action)))
    return v

def MIN_VALUE(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, MAX_VALUE(result(board, action)))
    return v

def minimax(board):

    player_name = player(board)

    if terminal(board):
        return None

    if board == initial_state():
        i, j = randint(0, 2), randint(0, 2)
        return (i, j)

    if player_name == X:
        value = -math.inf
        move = (-1, -1)
        for action in actions(board):
            minv = MIN_VALUE(result(board, action))
            if minv > value:
                value = minv
                move = action
        return move

    if player_name == O:
        value = math.inf
        move = (-1, -1)
        for action in actions(board):
            maxv = MAX_VALUE(result(board, action))
            if maxv < value:
                v = maxv
                move = action
        return move
