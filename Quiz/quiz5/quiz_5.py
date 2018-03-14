# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by JINGXUAN LI and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def get_paths():
    global grid
    path = defaultdict(int)
    if max_length <= 1:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path[1] += 1
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                L = [[] for _ in range(max_length)]
                W = [0 for _ in range(max_length)]
                if grid[i][j] == 1:
                    L[0].append((i, j))
                    n = 2
                    while n <= max_length:
                        L[n - 1], W[n - 1] = f(L[n - 2], n)
                        if n == max_length and len(L[n - 1]):
                            path[n] += len(L[n - 1])
                        n += 1
                    for e in range(max_length):
                        if W[e] != 0:
                            path[e] += W[e]
                    # print(W)
                    # print(f'({i},{j})-->{L}')
    return path


def f(P, n):
    Q = []
    count_no_next = 0
    for e in P:
        no_next = 1
        if e[1] > 0:
            if grid[e[0]][e[1]-1] == n:
                Q.append((e[0], e[1]-1))
                no_next = 0
        if e[0] > 0:
            if grid[e[0]-1][e[1]] == n:
                Q.append((e[0]-1, e[1]))
                no_next = 0
        try:
            if grid[e[0]][e[1]+1] == n:
                Q.append((e[0], e[1]+1))
                no_next = 0
        except Exception:
            pass

        try:
            if grid[e[0]+1][e[1]] == n:
                Q.append((e[0]+1, e[1]))
                no_next = 0
        except Exception:
            pass

        if no_next == 1:
            count_no_next += 1
    return Q, count_no_next




try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()

paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
