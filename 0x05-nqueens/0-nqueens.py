#!/usr/bin/python3
""" N queens """
import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

n_size = int(sys.argv[1])

def queens(size, i=0, a=None, b=None, c=None):
    """ Find possible positions """
    if a is None: a = []
    if b is None: b = []
    if c is None: c = []
    
    if i < size:
        for j in range(size):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(size, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

def solve(size):
    """ Solve the N queens problem """
    solution_set = []
    row = 0
    for solution in queens(size):
        for col in solution:
            solution_set.append([row, col])
            row += 1
        print(solution_set)
        solution_set = []
        row = 0

solve(n_size)
