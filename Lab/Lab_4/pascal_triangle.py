import sys


def pascal_triangle(height):
    tmp = height
    L = [[None] for _ in range(height)]
    if height == 1:
        # print(1)
        L = [1]
        return L
    else:
        # print(' '*(n-1), 1)
        L[0] = [1]
        while tmp - 1:
            tmp -= 1
            L[height - tmp - 1].append(0)
            L[height - tmp] = [L[height - tmp - 1][i - 1] + L[height - tmp - 1][i] for i in range(len(L[height - tmp - 1]))]
            # print(L[height - tmp])
    # 因为输入的时候要根据最大的字符长度 格式化每个元素的长度，所以不能直接输出，先存在L中。
    return L

height = input('Enter a nonnegative integer: ')
try:
    height = int(height)
    if height <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


X = pascal_triangle(height+1)
# print(X)
width = len(str(X[height][height//2]))
# print(width)
for n in range(height + 1):
    print(' '*(height - n)*width, end='')
    # print((' '*width).join(f'{X[n][e]:{width}d}' for e in range(n+1)
    print((' '*width).join('{:{width}}'.format(X[n][e], width = width) for e in range(n+1)))
