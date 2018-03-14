available_digits = input('Input a number that we will use as available digits: ')
desired_sum = input('Input a number that represents the desired sum: ')


def solution(input_num, sum_num):
    if input_num == 0:
        if sum_num == 0:
            return 1
        else:
            return 0
    if input_num < 0:
        return 0
    return (solution(input_num // 10, sum_num) + solution(input_num // 10, sum_num - input_num % 10))


n = 0
if sum(int(e) for e in list(available_digits)) < int(desired_sum):
    print('There is no solution.')
else:
    n = solution(int(available_digits), int(desired_sum))
    if n == 1:
        print('There is a unique solution.')
    else:
        print(f'There are {n} solutions.')
