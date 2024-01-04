#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board, N):
    solution = []
    for i in range(N):
        row = ""
        for j in range(N):
            row += "Q" if board[i][j] == 1 else "."
        solution.append(row)
    print("\n".join(solution))

def solve_nqueens(board, col, N):
    if col >= N:
        print_solution(board, N)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N)
            board[i][col] = 0

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
