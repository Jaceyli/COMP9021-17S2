import re

from stack_adt import Stack, EmptyStackError
from binary_tree_adt import BinaryTree

def parse_tree(expression):
    if any(not (c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    # Tokens can be natural numbers, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = parse_expression(tokens)
        return value
    except ZeroDivisionError:
        return



def parse_expression(tokens):
    s = Stack()
    p = {')': '(', ']': '[', '}': '{'}

    for i in tokens:
        try:
            i = BinaryTree(int(i))
        except ValueError:
            pass
        if i not in p:
            s.push(i)
        else:
            try:
                arg2 = s.pop()
                operator = s.pop()
                arg1 = s.pop()
                symbol = s.pop()
                if symbol != p[i]:
                    return
                tree = BinaryTree(operator)
                tree.left_node = arg1
                tree.right_node = arg2
                s.push(tree)
            except EmptyStackError:
                return
    if s.is_empty():
        return
    tree = s.pop()
    if s.is_empty():
        return tree
    else: return


parse_tree('[(1 - 20) + 300]').print_binary_tree()
# parse_tree('[(1 - 20) + 300]').evaluate()