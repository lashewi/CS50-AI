# """
# Tic Tac Toe Player
# """

# import math
# from copy import deepcopy
# from random import randint

# X = "X"
# O = "O"
# EMPTY = None


# def initial_state():
#     """
#     Returns starting state of the board.
#     """
#     return [[EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]


# def player(board):

#     xcounter = 0
#     ocounter = 0

#     for row in board:
#         xcounter += row.count(X)
#         ocounter += row.count(O)

#     return X if xcounter <= ocounter else O


# def actions(board):

#     possible_moves = set()

#     for i, row in enumerate(board):
#             for j, space in enumerate(row):
#                     possible_moves.add((i, j))

#     return possible_moves


# def result(board, action):

#     i, j = action
#     new_board = deepcopy(board)
#     current_player = player(new_board)

#     if new_board[i][j] is not EMPTY:
#         raise Exception("Not a valid action")
#     else:
#         new_board[i][j] = current_player

#     return new_board


# def winner(board):

#     #Rows 
#     for row in board:
#         xcounter = row.count(X)
#         ocounter = row.count(O)
#         if xcounter == 3:
#             return X
#         if ocounter == 3:
#             return O
    
#     #Columns
#     columns = []
#     for i in range(len(board)):
#         column = [row[i] for row in board]
#         columns.append(column)

#     for j in columns:
#         xcounter = j.count(X)
#         ocounter = j.count(O)
#         if xcounter == 3:
#             return X
#         if ocounter == 3:
#             return O

#     #Diag | Todo: Add better sol
#     if board[0][0] == O and board[1][1] == O and board[2][2] == O:
#         return O
#     if board[0][0] == X and board[1][1] == X and board[2][2] == X:
#         return X
#     if board[0][2] == O and board[1][1] == O and board[2][0] == O:
#         return O
#     if board[0][2] == X and board[1][1] == X and board[2][0] == X:
#         return X

#     # None | Todo: Modify to simplify terminal
#     return None

# def terminal(board):

#     if winner(board) is not None:
#         return True
#     else:
#         for row in board:
#             if EMPTY in row:
#                 return False
#         return True


# def utility(board):

#     if winner(board) == X:
#         return 1
#     elif winner(board) == O:
#         return -1
#     else:
#         return 0



# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     # min utility
#     alpha = -1
    
#     # max utility
#     beta = 1

#     def maxvalue(board, alpha, beta):
#         # if the board is the terminal board, return utility
#         if terminal(board):
#             return utility(board)
        
#         # else check for the action that returns the max utility
#         # perform linear search v initialized to -infinity
#         v = -100
#         # for each action,
#         # determine the highest of the min utilities of the resulting boards
#         # perform alpha-beta pruning
#         for action in actions(board):
#             v = max(v, minvalue(result(board, action), alpha, beta))

#             # if the current utility(v) is already the max utility, return it
#             if v >= beta:
#                 return v
            
#             # else recalibrate min utility to be max of (previous_min, current)
#             # 'cause max value wants the max of the mins being considered
#             alpha = max(alpha, v)

#         return v
    
#     def minvalue(board, alpha, beta):
#         if terminal(board):
#             return utility(board)
#         v = 100
#         for action in actions(board):
#             v = min(v, maxvalue(result(board, action), alpha, beta))
#             if v <= alpha:
#                 return v
#             beta = min(beta, v)
#         return v

#     # for the player (X or O)
#     # get the action that maximizes/minimizes the next utility
#     # recursively
#     if player(board) == X:
#         maxima = -100
#         for action in actions(board):
#             value = minvalue(result(board, action), alpha, beta)
#             if value > maxima:
#                 maxima = value
#                 optimal = action
#     else:
#         minima = 100
#         for action in actions(board):
#             value = maxvalue(result(board, action), alpha, beta)
#             if value < minima:
#                 minima = value
#                 optimal = action
 
#     return optimal



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
    """
    Returns player who has the next turn on a board.
    """

    # count the number of X's and O's
    cntX = 0
    cntO = 0

    for row in board:
        for value in row:
            if value == X:
                cntX += 1
            if value == O:
                cntO += 1                

    # X plays first so at any point in the game
    # X will always have played equal or greater no. of moves
    if cntX == cntO:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # empty set of action to avoid duplicates
    action = set()

    # add any cell that is not empty to the possible set of actions
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]

    # make a deep copy (copying each element by reference)
    # so that the actual board does not change
    new_board = deepcopy(board)

    # if the user tries to choose a non-empty cell
    if new_board[row][col] != EMPTY:
        raise "Invalid Move"
    
    # who's the player?
    who = player(new_board)

    # add 'who' to the chosen cell in the resulting board
    if who == X:
        new_board[row][col] = X
    else:
        new_board[row][col] = O
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # counters for the diagonals
    Xd1, Od1 = 0, 0
    Xd2, Od2 = 0, 0

    # check horizontal / main diagonal wins
    for row in range(3):

        # count X's and O's in each row
        Xr, Or = 0, 0
        for col in range(3):

            if board[row][col] == X:
                Xr += 1
            if board[row][col] == O:
                Or += 1

            if row == col:
                if board[row][col] == X:
                    Xd1 += 1
                if board[row][col] == O:
                    Od1 += 1
        
        if Xr == 3:
            return X
        if Or == 3:
            return O
    
    # check vertical wins and sub-diagonal
    # checking diagonal here because cramped up above
    for col in range(3):

        # count X's and O's in each column
        Xc, Oc = 0, 0
        for row in range(3):

            if board[row][col] == X:
                Xc += 1
            if board[row][col] == O:
                Oc += 1

            if row + col == 2:
                if board[row][col] == X:
                    Xd2 += 1
                if board[row][col] == O:
                    Od2 += 1
        
        if Xc == 3:
            return X
        if Oc == 3:
            return O
    
    if Xd1 == 3 or Xd2 == 3:
        return X
    if Od1 == 3 or Od2 == 3:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # if somebody won
    if winner(board) == X or winner(board) == O:
        return True
    
    # if no square is empty
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    
    if winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # min utility
    alpha = -1
    
    # max utility
    beta = 1

    def maxvalue(board, alpha, beta):
        # if the board is the terminal board, return utility
        if terminal(board):
            return utility(board)
        
        # else check for the action that returns the max utility
        # perform linear search v initialized to -infinity
        v = -100
        # for each action,
        # determine the highest of the min utilities of the resulting boards
        # perform alpha-beta pruning
        for action in actions(board):
            v = max(v, minvalue(result(board, action), alpha, beta))

            # if the current utility(v) is already the max utility, return it
            if v >= beta:
                return v
            
            # else recalibrate min utility to be max of (previous_min, current)
            # 'cause max value wants the max of the mins being considered
            alpha = max(alpha, v)

        return v
    
    def minvalue(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = 100
        for action in actions(board):
            v = min(v, maxvalue(result(board, action), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # for the player (X or O)
    # get the action that maximizes/minimizes the next utility
    # recursively
    if player(board) == X:
        maxima = -100
        for action in actions(board):
            value = minvalue(result(board, action), alpha, beta)
            if value > maxima:
                maxima = value
                optimal = action
    else:
        minima = 100
        for action in actions(board):
            value = maxvalue(result(board, action), alpha, beta)
            if value < minima:
                minima = value
                optimal = action
 
    return optimal