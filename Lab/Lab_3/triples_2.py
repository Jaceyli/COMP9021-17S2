import math
def f(n):
    flag = 0
    for e1 in range(0, int(math.sqrt(n+1))+1):
        for e2 in range(0, int(math.sqrt(n+1))+1):
            if e1**2 + e2**2 == n:
                flag = 1
                return e1, e2
            else:
                continue
    if flag == 0:
        return 0,0

for x in range(100,1000):
        a1, a2 = f(x)
        b1, b2 = f(x+1)
        c1, c2 = f(x+2)
        if a1+a2 != 0 and b1+b2 != 0 and c2+c2 != 0:
            print(f'({x}, {x+1}, {x+2}) (equal to ({a1}^2+{a2}^2, {b1}^2+{b2}^2, {c1}^2+{c2}^2)) is a solution.')




