# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021
# 0 10 2 7 52

import sys
from random import seed, randrange

from stack_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def explore_depth_first(x, y, target):
    # direction: 1:north, 2:east, 3:south, 4:west
    direction = 0
    if x > 0:
        direction = 1
    elif y > 0:
        direction = 2
    the_path = []
    used = set()
    stack = Stack()
    stack.push(tuple((x, y)))
    used.add(tuple((x, y)))
    sum = grid[x][y]

    if sum > target:
         return None

    while sum != target:
        if stack.is_empty():
            return None
        i, j = stack.peek()
        if i == 0 and direction == 1:
            direction = 2
            continue
        if i == 9 and direction == 3:
            direction = 4
            continue
        if j == 0 and direction == 4:
            direction = 1
            continue
        if j == 9 and direction == 2:
            direction = 3
            continue
        if direction == 1:
            i -= 1
        elif direction == 2:
            j += 1
        elif direction == 3:
            i += 1
        elif direction == 4:
            j -= 1

        if (i, j) in used:
            if direction < 4:
                direction += 1
            else:
                direction = 1
            continue
        if i == x and j == y:
            if direction < 4:
                direction += 1
            else:
                direction = 1
            continue
            # else:
            #     stack.pop()

        if sum + grid[i][j] <= target:
            sum += grid[i][j]
            stack.push(tuple((i, j)))
            used.add(tuple((i, j)))
        else:
            if direction < 4:
                direction += 1
            else:
                stack.pop()
        # print(stack.peek())

    while not stack.is_empty():
        the_path.append(stack.pop())
    the_path = the_path[::-1]
    # print(the_path)
    return the_path


try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()

path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
