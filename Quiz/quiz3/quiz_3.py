# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by JINGXUAN LI and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def add_l(q, n):
    if n != 0:
        exist = 0
        for e in q:
            if e[0] == n:
                exist = 1
                e[1] += 1
        if exist == 0:
            q.append([n, 1])
    return q


def notzero1(i, j, step):
    global grid
    flag = 1
    while step:
        if grid[i + step][j] == 0:
            flag = 0
            break
        step -= 1
    return flag


def notzero2(i, j, step):
    global grid
    flag = 1
    while step:
        if grid[i][j + step] == 0:
            flag = 0
            break
        step -= 1
    return flag


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def stairs_in_grid():
    global grid
    s = defaultdict(lambda: defaultdict(int))
    used = set()
    size = 1
    # max = math.ceil(len(grid) / 2) -1
    max = len(grid) + 1 / 2 if len(grid) % 2 else len(grid)/2
    while size <= max:
        l = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0 and (i, j) not in used and i + size < len(grid) and j + size < len(grid):
                    if grid[i][j + size] != 0 and notzero2(i, j, size):
                        x = i
                        y = j + size
                        count_steps = 0
                        while y + size < len(grid):
                            if x + size < len(grid) and y + size < len(grid):
                                # if grid[x + size][y] != 0 and grid[x + size][y + size] != 0:
                                if notzero1(x, y, size) and notzero2(x + size, y, size):
                                    count_steps += 1
                                    used.add((x + size, y))
                                    # print((x + size,y))
                                    x = x + size
                                    y = y + size
                                else:
                                    l = add_l(l, count_steps)
                                    break
                            else:
                                l = add_l(l, count_steps)
                                break
                        if y + size >= len(grid):
                            l = add_l(l, count_steps)
                else:
                    continue
        if l:
            s[size + 1] = l
        size += 1
        used.clear()

    return s
    # Replace return {} above with your code


# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
# print(stairs)
# stairs = {3: [[1, 4], [2, 6]], 2: [[1, 2], [2, 1]]}
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    # print(step_size)
    # print(stairs[step_size]
    stairs[step_size].sort(key=lambda x: (x[0]))
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
