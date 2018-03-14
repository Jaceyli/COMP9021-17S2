

'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3


def f(a, b):
    g = gcd(a, b)
    return(str(a//g)+'/'+ str(b//g))

def my_divison(z):
    w = z.split('/')
    return int(w[0])/ int(w[1])

def my_close(z):
    w = z.split('/')
    return abs(int(w[0])/ int(w[1]) - 0.5)

def my_sort_list(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if my_divison(lists[i]) > my_divison(lists[j]):
                lists[i], lists[j] = lists[j], lists[i]
    return lists

def my_sort_closest(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if my_close(lists[i]) > my_close(lists[j]):
                lists[i], lists[j] = lists[j], lists[i]
    return lists

for x in L:
    for y in L:
        if x <= y and y is not 0:
            if f(x, y) not in fractions:
                fractions.append(f(x, y))

my_sort_list(fractions)

fractions1 = fractions[:]
fractions1.pop()
fractions1.append('1')
clist = my_sort_closest(fractions)

if fractions1 == ['1']:
    closest_1 = 1
    print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:\n', ' ','1')
elif length > 1:
    if my_divison(fractions1[0]) == 0.0:
        fractions1.pop(0)
        fractions1.insert(0, '0')

    print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
    print('  ', '  '.join(e for e in fractions1))

    if max_value == 1:
        closest_1 = 0
        closest_2 = 1
    elif my_close(clist[0]) == 0:
        spot_on = True
    elif my_close(clist[0]) == my_close(clist[1]):
        closest_1 = my_sort_closest(fractions)[0]
        closest_2 = my_sort_closest(fractions)[1]
    else:
        closest_1 = my_sort_closest(fractions)[0]

if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')