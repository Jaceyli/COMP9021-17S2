from random import randint,seed

D = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
H = ['Five of a kind', 'Four of a kind', 'Full house', 'Straight', 'Three of a kind', 'Two pair', 'One pair', 'Bust']


def hand(l):
    C = [0 for _ in range(6)]
    for i in range(6):
        for e in l:
            C[i] = sum(1 for e in l if e[0] == f'{D[i]}')
    # print(C)
    if max(C) == 5:
        return 0
    elif max(C) == 4:
        return 1
    elif max(C) == 3:
        if 2 in C:
            return 2
        else: return 4
    elif max(C) == 2:
        if sum(1 for e in C if e == 2) == 2:
            return 5
        else: return 6
    else:
        tmp = set()
        for e in l:
            tmp.add(e[1])
        if tmp == {0, 1, 2, 3, 4} or tmp == {1, 2, 3, 4, 5}:
            return 3
        else:
            return 7


def play():
    tmp = [randint(0, 5) for _ in range(5)]
    # L = [D[e] for e in tmp]
    L = [[D[e], e] for e in tmp]
    L.sort(key=lambda x: [x[1], x[0]])
    # print(L)
    print('The roll is:', ' '.join(e[0] for e in L))
    print(f'It is a {H[hand(L)]}')
    count = 0
    while count < 2:
        if count == 0:
            myinput = input('Which dice do you want to keep for the second roll? ')
        else:
            myinput = input('Which dice do you want to keep for the third roll? ')
        if myinput == 'all' or myinput == 'All':
            print('Ok, done.')
            break
        else:
            if myinput.rstrip() == '':
                tmp = [randint(0, 5) for _ in range(5)]
                L = [[D[e], e] for e in tmp]
                L.sort(key=lambda x: [x[1], x[0]])
                print('The roll is:', ' '.join(e[0] for e in L))
                print(f'It is a {H[hand(L)]}')
                count += 1
            else:
                myinput = myinput.split(' ')
                if myinput == ['']:
                    print('kong')
                isp = ispossible(myinput, L[:])
                if isp == 1:
                    play_next(myinput, L)
                    count += 1
                    L.sort(key=lambda x: [x[1], x[0]])
                    print('The roll is:', ' '.join(e[0] for e in L))
                    print(f'It is a {H[hand(L)]}')
                elif isp == 2:
                    print('Ok, done.')
                    break
                else:
                    print('That is not possible, try again!')
                    continue


def play_next(m, l):
    for i in range(5):
        if l[i][0] not in m:
            t = randint(0, 5)
            l[i] = [D[t],t]
        else:
            m.remove(l[i][0])
    return l


def ispossible(m,l):
    l1 =[]
    for x in l:
        l1.append(x[0])
    if sorted(l1) == sorted(m):
        return 2
    else:
        for e in m:
            if e in l1:
                l1.remove(e)
            else:
                return 0
        return 1

# seed(0)
def simulate(n):
    times = [0 for _ in range(8)]
    n1 = n
    while n1:
        tmp = [randint(0, 5) for _ in range(5)]
        Q = [[D[e], e] for e in tmp]
        times[hand(Q)] += 1


        # for e in Q:
        #     print(e[1],end= ' ')
        # print('------',H[hand(Q)])


        n1 -= 1
    times.pop()
    for i in range(7):
        print(f'{H[i]}'.ljust(15), end='')
        print(f': {times[i]/n*100:.2f}%')




# 为啥print(e for e in L)不行？？必须join？？


# print(' '.join(D[e] for e in L))

# play()
# simulate(100)
# hand([['Ace', 0], ['Queen', 2], ['Jack', 3], ['King', 1], ['10', 4]])
