
import re

from stack_adt import Stack, EmptyStackError
from binary_tree_adt import BinaryTree


'''
Uses the Stack and BinaryTree interfaces to build an expression tree and evaluate
an arithmetic expression written in infix, fully parenthesised with parentheses,
brackets and braces, and built from natural numbers using the binary +, -, * and / operators.
'''


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
    parentheses = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    # tree = BinaryTree()
    for token in tokens:
        try:
            token = BinaryTree(int(token))
        except ValueError:
            pass
        if token not in parentheses:
            stack.push(token)
        else:
            try:
                arg_2 = stack.pop()
                operator = stack.pop()
                arg_1 = stack.pop()
                symbol = stack.pop()
                if symbol != parentheses[token]:
                    return
                tree = BinaryTree(operator)
                tree.left_node = arg_1
                tree.right_node = arg_2
                stack.push(tree)
                # stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[operator](arg_1, arg_2))
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    tree = stack.pop()
    if not stack.is_empty():
        return
    return tree

parse_tree('[(1 - 20) + 300]').print_binary_tree()
parse_tree('[(1 - 20) + 300]').evaluate()