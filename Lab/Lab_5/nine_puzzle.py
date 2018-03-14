


def validate_9_puzzle(grid):
    s = set()
    for e in grid:
        for x in e:
            if x is None:
                x = 0
            s.add(x)
    if s == set(range(0, 9)):
        print('This is a valid 9 puzzle, and it is solvable')
    else:
        print('This is an invalid or unsolvable 9 puzzle')

def solve_9_puzzle(grid):
    pass


# validate_9_puzzle([[1, 2, 3], [4, 5, 6], [None, 7, 8]])