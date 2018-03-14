
'''
Implements a function that takes as input an iterable L of nonnegative integers and an integer N,
and displays all ways of inserting negations and parentheses in L, resulting in an expression
that evaluates to N.
'''


def subtractions(L, N):
    for expression in possible_subtractions(L):
        if eval(expression) == N:
            print(expression[1: -1])

def possible_subtractions(L):
    if len(L) == 1:
        return (str(L[0]),)
    return (''.join(['(', e1, '-', e2, ')'])
            for i in range(1, len(L))
                for e1 in possible_subtractions(L[:i])
                    for e2 in possible_subtractions(L[i:]))



subtractions((1, 3, 2, 5, 11, 9, 10, 8, 4, 7, 6), 40)