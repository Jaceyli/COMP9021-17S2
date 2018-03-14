from math import sqrt

L = [6, 5, 4, 3, 2, 1]
r = [3, 2, 1]


def turn_right(top, front, right, n):
    n %= 4
    if n == 0:
        return top, front, right
    elif n == 1:
        return L[right - 1], front, top
    else:
        return turn_right(L[right - 1], front, top, n - 1)


def turn_left(top, front, right, n):
    n %= 4
    if n == 0:
        return top, front, right
    elif n == 1:
        return right, front, L[top - 1]
    else:
        return turn_left(right, front, L[top - 1], n - 1)


def turn_up(top, front, right, n):
    n %= 4
    if n == 0:
        return top, front, right
    elif n == 1:
        return front, L[top - 1], right
    else:
        return turn_up(front, L[top - 1], right, n - 1)


def turn_down(top, front, right, n):
    n %= 4
    if n == 0:
        return top, front, right
    elif n == 1:
        return L[front - 1], top, right
    else:
        return turn_down(L[front - 1], top, right, n - 1)


while True:
    number = input('Enter the desired goal cell number: ')
    try:
        number = int(number)
        if number <= 0:
            print('Incorrect value, try again')
            continue
        else:
            break
    except ValueError:
        print('Incorrect value, try again')

square = int(sqrt(number))
# print(f'square:{square}')
remain = number - square ** 2
# print(f'remain:{remain}')
if square > 1:
    for e in range(1, square + 1):
        if e == 1:
            r = turn_right(*r, e)
            r = turn_down(*r, e)
            # print(f'R{e},D{e}')
        elif e == square:
            if square % 2:
                r = turn_right(*r, e - 1)
                # print(f'R{e - 1}')
            else:
                r = turn_left(*r, e - 1)
                # print(f'L{e - 1}')
        elif e % 2:
            r = turn_right(*r, e)
            r = turn_down(*r, e)
            # print(f'R{e},D{e}')
        else:
            r = turn_left(*r, e)
            r = turn_up(*r, e)
            # print(f'L{e},U{e}')

if remain == 0:
    print(f'On cell {number}, {r[0]} is at the top, {r[1]} at the front, and {r[2]} on the right.')
elif square % 2:
    r = turn_right(*r, 1)
    # print('R1')
    if remain == 1:
        print(f'On cell {number}, {r[0]} is at the top, {r[1]} at the front, and {r[2]} on the right.')
    elif remain - 1 <= square:
        r = turn_down(*r, remain - 1)
        # print(f'D{remain -1}')
        print(f'On cell {number}, {r[0]} is at the top, {r[1]} at the front, and {r[2]} on the right.')
    else:
        r = turn_down(*r, square)
        r = turn_left(*r, remain - square - 1)
        # print(f'D{square},L{remain -square -1}')
        print(f'On cell {number}, {r[0]} is at the top, {r[1]} at the front, and {r[2]} on the right.')
else:
    r = turn_left(*r, 1)
    # print('L1')
    if remain == 1:
        print(f'On cell {number}, {r[0]} is at the top, {r[1]} at the front, and {r[2]} on the right.')
    elif remain - 1 <= square:
        r = turn_up(*r, remain - 1)
        # print(f'U{remain -1}')
        print(f'On cell {number}, {r[0]} is at the top, {r[1]} at the front, and {r[2]} on the right.')
    else:
        r = turn_up(*r, square)
        r = turn_right(*r, remain - square - 1)
        # print(f'U{square},R{remain -square -1}')
        print(f'On cell {number}, {r[0]} is at the top, {r[1]} at the front, and {r[2]} on the right.')
