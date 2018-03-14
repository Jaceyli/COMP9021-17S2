'''
Every strictly positive integer N can be uniquely coded as a string sigma
of 0's and 1's ending with 1, so of the form b_2b_3...b_k with k >= 2 and b_k = 1,
such that N is the sum of all F_i's, 2 <= i <= k, with b_i = 1.

Moreover:
- there are no two successive occurrences of 1 in sigma;
- F_k is the largest Fibonacci number that fits in N, and
  if j is the largest integer in {2,...,k-1} such that b_j = 1
  then F_j is the largest Fibonacci number that fits in N - F_k, and
  if i is the largest integer in {2,...,j-1} such that b_i = 1
  then F_i is the largest Fibonacci number that fits in  N - F_k - F_j...

Also, every string of 0's and 1's ending in 1 and having no two
successive occurrences of 1's is a code of a strictly positive integer
according to this coding scheme. For instance:
- There is only one string of 0's and 1's of length 1 ending in 1 and
  having no two successive occurrences of 1's; it is 1, and it codes 1.
- There is only one string of 0's and 1's of length 2 ending in 1 and
  having no two successive occurrences of 1's; it is 01, and it codes 2.
- The strings of 0's and 1's of length 3 ending in 1 and having no two successive occurrences
  of 1's are 001 and 101 and they code 3 and 4, respectively.
- The strings of 0's and 1's of length 4 ending in 1 and having no two successive occurrences
  of 1's are 0001, 1001 and 0101 and they code 5, 6 and 7, respectively.
- The strings of 0's and 1's of length 5 ending in 1 and having no two successive occurrences
  of 1's are 00001, 10001, 01001, 00101 and 10101 and they code 8, 9, 10, 11 and 12, respectively.
- ...

The Fibonacci code of N adds 1 at the end of sigma; the resulting string then ends in two 1's,
therefore marking the end of the code, and allowing one to let one string code a finite sequence
of strictly positive integers. For instance, 00101100111011 codes (11,3,4).
'''


def encode(n):
    '''
    Retuns the Fibonacci code of n, meant to be a strictly positive integer.
    '''
    fibo = get_fibonacci_list(n)
    code = ['0' for _ in range(len(fibo))] + ['1']
    # print(fibo, code)
    for i in range(len(fibo) - 1, -1, -1):
        if fibo[i] <= n:
            n -= fibo[i]
            code[i] = '1'
    print(''.join(code))


def decode(code):
    '''®
    The argument is meant to be a string of 0's and 1's.
    Returns 0 if the argument cannot be a Fibonacci code;
    otherwise returns the integer argument is the Fibonacci code of.
    '''
    if len(code) < 2 or code[-2:] != '11':
        print(0)

    elif 2 in [int(code[i]) + int(code[i + 1]) for i in range(len(code) - 2)]:
        print(0)
    else:
        fibo = get_fibonacci_list_by_len(len(code) - 1)
        num = 0
        for i in range(len(fibo)):
            # print(fibo[i],code[i])
            num += int(fibo[i]) * int(code[i])
        print(num)



def get_fibonacci_list(n):
    fibo = []
    current = 1
    previous = 0
    while current + previous <= n:
        sum = current + previous
        previous = current
        current = sum
        fibo.append(sum)
    return fibo

def get_fibonacci_list_by_len(length):
    fibo = []
    current = 1
    previous = 0
    i = 0
    while i < length:
        i += 1
        sum = current + previous
        previous = current
        current = sum
        fibo.append(sum)
    return fibo
decode('100011011')