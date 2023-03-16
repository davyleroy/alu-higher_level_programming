#!/usr/bin/python3
"""Module is to solve the N-Queens challenge problem"""
from sys import argv


def checkspot(board, r, c):
    n = len(board) - 1
    if board[r][c]:
        return 0
    for row in range(r):
        if board[row][c]:
            return 0
    i = r
    j = c
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if board[i][j]:
            return 0
    i = r
    j = c
    while i > 0 and j < n:
        i -= 1
        j += 1
        if board[i][j]:
            return 0
    return 1


def initboard(n=4):
    b = []
    for r in range(n):
        b.append([0 for c in range(n)])
    return b


def findsoln(board, row):
    for col in range(len(board)):
        if checkspot(board, row, col):
            board[row][col] = 1
            if row == len(board) - 1:
                print(convtosoln(board))
                board[row][col] = 0
                continue
            if findsoln(board, row + 1):
                return board
            else:
                board[row][col] = 0
    return None


def convtosoln(board):
    soln = []
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c]:
                soln.append([r, c])
    return soln


def nqueens(n=4):
    for col in range(n):
        board = initboard(n)
        board[0][col] = 1
        findsoln(board, 1)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(n)
