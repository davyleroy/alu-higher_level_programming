#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def n_queens(n):
    if not n.isdigit():
        print("n must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("n must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        for r, c in board:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def solve(board, row):
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                solve(board + [[row, col]], row + 1)

    solve([], 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: n_queens n")
        sys.exit(1)
    n_queens(sys.argv[1])
