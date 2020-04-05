import sys
import numpy as np


initial_board = [
    [3,1,0,8,0,9,0,4,5],
    [0,0,0,1,0,6,0,0,0],
    [5,0,9,0,0,0,1,0,6],
    [0,0,0,9,0,7,0,0,0],
    [0,8,0,0,0,0,0,2,0],
    [0,0,0,5,0,2,0,0,0],
    [8,0,2,0,0,0,4,0,9],
    [0,0,0,3,0,1,0,0,0],
    [4,5,0,2,0,8,0,6,3]
]

a_square = [(0,2), (0,2)]
b_square = [(0,2), (3,5)]
c_square = [(0,2), (6,8)]
d_square = [(3,5), (0,2)]
e_square = [(3,5), (3,5)]
f_square = [(3,5), (6,8)]
g_square = [(6,8), (0,2)]
h_square = [(6,8), (3,5)]
i_square = [(6,8), (6,8)]

sudoku_numbers = [1,2,3,4,5,6,7,8,9]

dimension_of_board = len(initial_board)

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def solve(board):
    # Here we get the solution of the initial_board...
    spot = pick_a_empty_space(board)
    if not spot:
        return True
    for pos_number in numbers_remaning(board[spot[0]]):
        if check_spot_conditions(pos_number, spot, board):
            board[spot[0]][spot[1]] = pos_number
            if solve(board):
                return True
            board[spot[0]][spot[1]] = 0
    return False

def numbers_remaning(row):
    remaining_numbers = []
    for number in sudoku_numbers:
        if number not in row:
            remaining_numbers.append(number)
    return remaining_numbers

def pick_a_empty_space(board):
    # This is gonna pick the first square empty on the board(l->r;t->b)...
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)
            else:
                continue
    return False

def row_condition_accomplish(row, number_to_try):
    for element in row:
        if element is not number_to_try:
            continue
        else:
            return False
    return True

def col_condition_accomplish(col, number_to_try):
    for element in col:
        if element is not number_to_try:
            continue
        else:
            return False
    return True


def square_condition_accomplish(square_board, number_to_try):
    for row in square_board:
        for number in row:
            if number == number_to_try:
                return False
            else: 
                continue
    return True

def get_space_square(space):
    # This check the corresponding square in the board...
    if space[0] <= 2:
        if space[1] <= 2:
            return a_square
        elif space[1] <= 5:
            return b_square
        else:
            return c_square 
    elif space[0] <=5 :
        if space[1] <= 2:
            return d_square
        elif space[1] <= 5:
            return e_square
        else:
            return f_square
    else:
        if space[1] <= 2:
            return g_square
        elif space[1] <= 5:
            return h_square
        else:
            return i_square

def get_board_square(board, square_in):
    square_board = []
    for row_index in range(square_in[0][0], square_in[0][1]+1):
        colums_to_append = []
        for col_index in range(square_in[1][0], square_in[1][1]+1):
            colums_to_append.append(board[row_index][col_index])
        square_board.append(colums_to_append)
    return square_board

def check_spot_conditions(number, space, board):
    col = []
    for i in range(len(board)):
        col.append(board[i][space[1]])
    if row_condition_accomplish(board[space[0]], number) and col_condition_accomplish(col, number):
        if square_condition_accomplish(get_board_square(board, get_space_square(space)), number):
            return True
        # Is a possible number...return it
    else:
        return False
        # return not possible(sorry)


def main(board):
    if solve(board):
        print_board(board)
    else:
        print("No solution found to this board")
# In here we need to put later the menu, UI part and solving game... 

if __name__ == '__main__':
    main(initial_board)