import sys
# print(ord('Z'))
# print(chr(90))


def triangle(n):
    for e in range(1, n+1):
        L = [i for i in range(sum(list(range(e)))+1, sum(list(range(e+1)))+1)]
        L1 = L[:-1]
        L1 = L1[::-1]
        L.extend(L1)

        y = n - e
        print(' '*y, end="")

        print(''.join(chr((x-1) % 26+65) for x in L))


height = input('Enter strictly positive number: ')
try:
    height = int(height)
    if height < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

triangle(height)