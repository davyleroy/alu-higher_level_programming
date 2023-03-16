#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ']*n for i in range(n)]

def is_safe(board, row, col, n):
    """Check if placing a queen at row, col is safe."""
    # check row and column
    for i in range(n):
        if board[row][i] == 'Q' or board[i][col] == 'Q':
            return False
    # check diagonals
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row+1, n), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row+1, n), range(col+1, n)):
        if board[i][j] == 'Q':
            return False
    return True

def recursive_solve(board, col, n, solutions):
    """Recursively solve an N-queens puzzle."""
    if col == n:
        solutions.append([[i,j] for i,row in enumerate(board) for j,val in enumerate(row) if val=='Q'])
        return solutions
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            recursive_solve(board, col+1, n, solutions)
            board[row][col] = ' '
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("N must be an integer greater than or equal to 4.")
        sys.exit(1)

    n = int(sys.argv[1])
    board = init_board(n)
    solutions = recursive_solve(board, 0, n, [])
    for sol in solutions:
        print(sol)

