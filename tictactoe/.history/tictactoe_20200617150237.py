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
                if board[i][j] == EMPTY:
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



def minimax(board):

    alpha = -math.inf
    beta = math.inf

    def maxvalue(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, minvalue(result(board, action), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def minvalue(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, maxvalue(result(board, action), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    if player(board) == X:
        maxima = -math.inf
        for action in actions(board):
            value = minvalue(result(board, action), alpha, beta)
            if value > maxima:
                maxima = value
                optimal = action
    else:
        minima = math.inf
        for action in actions(board):
            value = maxvalue(result(board, action), alpha, beta)
            if value < minima:
                minima = value
                optimal = action
 
    return optimal