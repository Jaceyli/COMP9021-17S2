# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by *** and Eric Martin for COMP9021


import sys
import copy
from random import seed, sample

from priority_queue_adt import *


def delete_one(pq1, element):
    if pq1.is_empty():
        raise EmptyPriorityQueueError('Cannot delete element from empty priority queue')
    for i in range(len(pq1._data)):
        if pq1._data[i] == element:
            pq1._data[i], pq1._data[pq1._length] = pq1._data[pq1._length], pq1._data[i]
            pq1._length -= 1
            pq1._bubble_down(i)
            break


preferred_ordering =[]

def preferred_sequence():
    if pq.is_empty():
        return preferred_ordering[::-1]
    for e in pq._data:
        pq1 = copy.deepcopy(pq)
        if e:
            delete_one(pq1, e)
            pq1.insert(e)
            if pq._data == pq1._data:
                preferred_ordering.append(e)
                delete_one(pq, e)
                return preferred_sequence()


try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())

