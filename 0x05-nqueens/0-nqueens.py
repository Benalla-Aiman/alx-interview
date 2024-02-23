#!/usr/bin/python3
'''N Queens Challenge'''

import sys

def solve(n):
    positions = [-1] * n
    place_queen(positions, 0, n)

def place_queen(positions, target_row, n):
    if target_row == n:
        print_board(positions)
        return

    for column in range(n):
        if check_place(positions, target_row, column):
            positions[target_row] = column
            place_queen(positions, target_row + 1, n)

def check_place(positions, ocuppied_rows, column):
    for i in range(ocuppied_rows):
        if positions[i] == column or \
            positions[i] - i == column - ocuppied_rows or \
            positions[i] + i == column + ocuppied_rows:
            return False
    return True

def print_board(positions):
    for row in range(n):
        line = ""
        for column in range(n):
            if positions[row] == column:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

n = int(sys.argv[1])
solve(n)