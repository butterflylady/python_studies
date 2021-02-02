def sudoku_solver(board):
    """
    Solves a sudoku board using backtracking
    :param board: 2D list of integers between 1 and 9
    :return: solution
    """


# Print the board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == len(board[0]) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Find the empty location on the board and return its indices (i, j) (row, col)
def find_empty_location(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return False


# Check if the number is in the row
def num_used_in_row(board, row, num):
    if num in board[row]:
        return True
    return False


# Check if the number is in the col
def num_used_in_col(board, col, num):
    if num in [row[col] for row in board]:
        return True
    return False


# Check if the number is in the box 3x3
def num_used_in_box(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[(row // 3) * 3 + i][(col // 3) * 3 + j] == num:
                return True
    return False


# Check if  the number is not placed in current row, current column or current box 3x3
def check_if_location_is_possible(board, row, col, num):
    return not num_used_in_row(board, row, num) and \
           not num_used_in_col(board, col, num) and \
           not num_used_in_box(board, row, col, num)


# Takes a partially filled-in board and attempts to assign numbers from 1 to 9 to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def solve_sudoku(board):
    find = find_empty_location(board)
    if not find:
        return True
    else:
        row, col = find
    for num in range(1, 10):
        if check_if_location_is_possible(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


if __name__ == '__main__':
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # If success print the board (solution)
    if solve_sudoku(board):
        print(print_board(board))
    else:
        print("There is no solution for this board!")
