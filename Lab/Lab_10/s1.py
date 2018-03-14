def subtractions(L, N):
    for sub in possible_subtractions(L):
        # print(sub)
        if eval(sub) == N:
            print(sub[1:-1])


def possible_subtractions(L):
    if len(L) == 1:
        return (str(L[0]),)
    return (''.join(['(', e1, '-', e2, ')'])
            for i in range(1, len(L))
                for e1 in possible_subtractions(L[i:])
                    for e2 in possible_subtractions(L[:i])
    )



subtractions((1, 3, 2, 5, 11, 9, 10, 8, 4, 7, 6), 40)