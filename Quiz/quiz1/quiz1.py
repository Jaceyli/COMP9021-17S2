# Written by JINGXUAN LI and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''


import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

# L1 = L The assignment just copies the reference to the list
# slice it:

L1 = L[:]
L2 = L[:]
# I: index of elements that used
I = []
M = []
N = []

# ------M------
if(length != 0):
  M.append(L1.pop(int(length/2)))
  if (length % 2) != 0: 
    while (len(L1)):
      M.append(L1.pop(0))
      M.append(L1.pop())
  else:
    while (len(L1)-1):
      M.append(L1.pop(0))
      M.append(L1.pop())
    M.append(L1.pop())

# ------N------
if(length != 0):
  num = L2[0]
  N.append(num) 
  I.append(0)
  while(len(I) < length):
    if(num < length and num not in I):
      I.append(num)
      num = L2[num]
      N.append(num)
    else:
      for e in range(0,length):
        if (e not in I):
          num = e
          break;
      I.append(num)
      num = L2[num]
      N.append(num)
  
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)
