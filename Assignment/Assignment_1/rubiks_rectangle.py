from collections import deque
import sys

L = [1, 2, 3, 4, 5, 6, 7, 8]
D = deque()
D.append([L, 0])


# row_exchange
def transform1(l):
    l.reverse()
    return l


# right_circular_shift
def transform2(l):
    tmp1 = l.pop(3)
    tmp2 = l.pop(3)
    l.insert(0, tmp1)
    l.append(tmp2)
    l1 = l.copy
    return l1()


# middle_clockwise_rotation
def transform3(l):
    tmp = l[1]
    l[1] = l[-2]
    l[-2] = l[-3]
    l[-3] = l[2]
    l[2] = tmp
    l2 = l.copy()
    return l2


def rubik_solution(d):
    s = set()
    s.add(str(d[0][0]))
    while 1:
        l = d.popleft()
        l[1] += 1
        
        tmp1 = transform1(l[0].copy())
        if tmp1 != L_final and str(tmp1) not in s:
            d.append([tmp1, l[1]])
            s.add(str(tmp1))
        elif tmp1 == L_final:
            return l[1]
    
        tmp2 = transform2(l[0].copy())
        if tmp2 != L_final and str(tmp2) not in s:
            d.append([tmp2, l[1]])
        elif tmp2 == L_final:
            return l[1]
    
        tmp3 = transform3(l[0].copy())
        if tmp3 != L_final and str(tmp3) not in s:
            d.append([tmp3, l[1]])
        elif tmp3 == L_final:
            return l[1]


L_final = []
num = ['1', '2', '3', '4', '5', '6', '7', '8']
myinput = input('Input final configuration: ')
for e in myinput:
    if e.isdigit() and e in num:
        num.remove(e)
        L_final.append(int(e))
    elif e is ' ':
        pass
    else:
        print('Incorrect configuration, giving up...')
        sys.exit()

if L == L_final:
    step = 0
else:
    step = rubik_solution(D)

if step <= 1:
    print(f"{step} step is needed to reach the final configuration.")
else:
    print(f"{step} steps are needed to reach the final configuration.")
