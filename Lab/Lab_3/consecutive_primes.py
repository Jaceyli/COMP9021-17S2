import math

L = [x for x in range(10000, 100000) if 0 not in [x % e for e in range(2, int(math.sqrt(x)) + 1)]]
print('The solutions are:\n')
for e in range(1, len(L) - 5):
    if L[e] == L[e + 1] - 2 and L[e + 1] == L[e + 2] - 4 and L[e + 2] == L[e + 3] - 6 and L[e + 3] == L[e + 4] - 8 and \
                    L[e + 4] == L[e + 5] - 10:
        print('   ', L[e], L[e + 1], L[e + 2], L[e + 3], L[e + 4], L[e + 5])
