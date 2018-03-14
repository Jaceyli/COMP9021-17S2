# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children, and
# - the sum of the nodes along all of T*'s branches is equal to M.
#
# Written by JINGXUAN and Eric Martin for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)

def expand_tree(tree, n):
    if n == -1:
        n = tree.value
    if n != the_max:
        if tree.left_node.value:
            expand_tree(tree.left_node, n + tree.left_node.value)
            if not tree.right_node.value:
                tree.right_node = BinaryTree(the_max - n)
        if tree.right_node.value:
            expand_tree(tree.right_node, n + tree.right_node.value)
            if not tree.left_node.value:
                tree.left_node = BinaryTree(the_max - n)
        if not (tree.right_node.value and tree.left_node.value):
            tree.left_node = BinaryTree(the_max - n)
            tree.right_node = BinaryTree(the_max - n)


def max_branch(tree, n):
    L.append(n)
    if n == -1:
        n = tree.value
    if tree.left_node.value:
        max_branch(tree.left_node, n + tree.left_node.value)
    if tree.right_node.value:
        max_branch(tree.right_node, n + tree.right_node.value)


                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
L = []

if tree.height() > 0:
    max_branch(tree, -1)
    the_max = max(L)
    expand_tree(tree, -1)

print('Here is the expanded tree:')
tree.print_binary_tree()



