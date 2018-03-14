def solution(l, sequence, code):
    # print(sequence, code)
    if not sequence:
        return []
    for e in list(sequence):
        if e == chr(code + 1):
            l.append(e)
            return solution(l, sequence, code + 1)
    return l

sequence = input('Please input a string of lowercase letters: ')
# print(ord('a'))
# print(chr(97))
l1 = []
for e in list(sequence):
    l = [e]
    l1.append(solution(l, sequence, ord(e)))
maxlen = max(len(e) for e in l1)
for e in l1:
    if len(e) == maxlen:
        print('The solution is:',''.join(i for i in e))
        break
