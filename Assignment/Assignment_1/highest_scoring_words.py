import sys

dic = {'a': 2, 'b': 5, 'c': 4, 'd': 4, 'e': 1, 'f': 6, 'g': 5, 'h': 5, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 5,
       'n': 2, 'o': 3, 'p': 5, 'q': 7, 'r': 2, 's': 1, 't': 2, 'u': 4, 'v': 6, 'w': 6, 'x': 7, 'y': 5, 'z': 7}
new_wordsEn = []
word = {}
L = []
# tmp = []
# L = ['a', 'e', 'i', 'o', 'u']
# L = ['e','a','e','o', 'r','t','s','m','n']

fo = open("wordsEn.txt")
filelines = fo.readlines()


def word_value(w):
    return sum(dic[e] for e in w)

myinput = input('Enter between 3 and 10 lowercase letters: ')
for e in myinput:
    if e.isalpha() and e.islower():
        L.append(e)
    elif e is ' ':
        pass
    else:
        print('Incorrect input, giving up...')
        sys.exit()
if len(L) <3 or len(L) > 10:
    print('Incorrect input, giving up...')
    sys.exit()

for line in filelines:
    line = line.rstrip()
    flag = 1
    L1 = L[:]
    for e in line:
        if e not in L1:
            flag = 0
            break
        else:
            L1.remove(e)
            flag = 1
    if flag == 1:
        word[line] = word_value(line)

if word:
    max_value = max(word.items(), key=lambda x: x[1])
    print(f'The highest score is {max_value[1]}.')
    count = 0
    keys = []
    for key,value in word.items():
        if value == max_value[1]:
            count += 1
            keys.append(key)
    if count > 1:
        print('The highest scoring words are, in alphabetical order:')
        for e in keys:
            print('   ', e)
    else:
        print(f'The highest scoring word is {keys[0]}')
else:
    print('No word is built from some of those letters.')

fo.close()