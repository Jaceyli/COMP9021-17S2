def fab(height):
    L = [[None] for _ in range(height)]
    tmp = height
    if height == 1:
        return('1')
    else:
        L[0] = [1] 
        while(tmp - 1):
            tmp -= 1
            L[height - tmp - 1].append(0)
            L[height - tmp] = [L[height - tmp -1][e-1] + L[height - tmp -1][e] for e in range(len(L[height - tmp -1]))]
        return L
h = 5
X = fab(h+1)
##print(X)
width = len(str(X[h][h//2]))
for e in range(h+1):
    print(' '*width*(h - e),end = '')
##    print((' '*width).join(f'{X[e][i]:{width}d}' for i in range(e + 1)))
    print((' '*width).join('{:{width}}'.format(X[e][i], width = width) for i in range(e+1)))

    
