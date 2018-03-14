def solution(first, second, target):
    # print(first, second, target)
    if not target:
        return True
    if first == target:
        return True
    if second == target:
        return True
    if not first or not second:
        return False
    if first[0] == target[0] and solution(first[1:], second, target[1:]):
        return True
    if second[0] == target[0] and solution(first, second[1:], target[1:]):
        return True
    return False


max = 'third'
bigger = 'second'
nums= 'first', 'second', 'third'
strings = [input(f'Please input the {num} string: ') for num in nums]
if len(strings[0]) > len(strings[1]):
    strings[0], strings[1] = strings[1], strings[0]
    bigger = 'first'
if len(strings[1]) > len(strings[2]):
    strings[1], strings[2] = strings[2], strings[1]
    max = bigger
# print(strings)
if len(strings[0]) + len(strings[1]) < len(strings[2]) or not solution(strings[0], strings[1], strings[2]):
    print('No solution')
else:
    print(f'The {max} string can be obtained by merging the other two.')


