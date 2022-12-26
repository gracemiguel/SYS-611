# -*- coding: utf-8 -*-
"""
SYS-611: Tic-Tac-Toe Example

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the python3 behavior for importing, division, and printing in python2
from __future__ import absolute_import, division, print_function

# import the pandas library and refer to it as `pd`
import pandas as pd
import numpy as np

# define the game state as a list of lists with 3x3 grid cells
# initialize the cells to a blank space character
state = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
# define a function to check if a mark is valid
def is_valid(row, col):
    # check if the row/column is empty
    return state[row][col] == " "

# define a function to mark an 'x' at a row and column
def mark_x(row, col):
    # check if this is a valid move
    if is_valid(row, col):
        # if valid, update the state accordingly
        state[row][col] = "x"

# define a function to mark an 'o' at a row and column
def mark_o(row, col):
    # check if this is a valid move
    if is_valid(row, col):
        # if valid, update the state accordingly
        state[row][col] = "o"

# define a function to print out the grid to the console
def show_grid():
    # use the pandas dataframe to help format the matrix
    print(pd.DataFrame(state))

# define a function to clear out the game state
def reset_game():
    # iterate over values in 0, 1, 2
    for i in range(3):
        # iterate over values in 0, 1, 2
        for j in range(3):
            # empty this state location at (i,j)
            state[i][j] = " "

def checkColumns(state):
    df = pd.DataFrame(state)
    for col in df:
        if(" " in df[col]):
            pass
        else:
            values = df[col].values

            result = np.all(values == values[0])
            if(result):
                return values[0]
            elif col <= len(df):
                pass
            else:
                return ""

def checkRows(state):
    df = pd.DataFrame(state)
    count = 0
    for index, row in df.iterrows():
        values = row.to_numpy()
        result = np.all(values == values[0])
        if(result):
            return values[0]
        elif len(row) <= len(df):
            pass
        else:
            return ""

def checkDiagonal(state):
    df = pd.DataFrame(state)
    left_corner = df[0][0]
    right_corner = df[2][2]
    count1 = 0
    count2 = 0
    for i in range(3):
        if df[i][i] == left_corner:
            count1+=1
        if count1 == 3:
            return(left_corner)
        else:
            pass
    for i in range(2):
        if df[i][2-i] == right_corner:
            count2+=1
        if count2 == 3:
            return(right_corner)
        elif i<2:
            pass
        else:
            return ""




def get_winner():
    result = ""
    if(checkRows(state) == 'x' or checkRows(state) == 'o'):
        result = checkRows(state)
        print(result)
        return result
    elif(checkColumns(state) == 'x' or checkColumns(state) == 'o'):
        result = checkColumns(state)
        print(result)
        return result
    elif(checkDiagonal(state) == 'x' or checkDiagonal == "o"):
        result = checkDiagonal(state)
        print(result)
        return result
    else:
        print("")
        return False



def is_tie():
    if(get_winner() == ""):
        print(True)
        return True
    else:
        print(False)
        return False
    pass # replace this line for HW-01

#%% example game sequence

mark_x(0, 0)
show_grid()

mark_x(1, 1)
show_grid()

mark_x(2, 2)
show_grid()

mark_o(2,0)
show_grid()

mark_o(2, 2)
show_grid()

mark_o(2,1)
show_grid()

show_grid()
get_winner()
is_tie()

# reset_game()
# show_grid()