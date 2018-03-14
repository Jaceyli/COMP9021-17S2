import re
from operator import add, sub, mul, truediv

from stack_adt import Stack, EmptyStackError


def evaluate(expression):
    if any(not (e.isdigit() or e.isspace() or e in '(){}[]+-*/') for e in expression):
        print('error')
    token = re.findall('\d+|\{|\}|\(|\)|\[|\]|\+|\-|\*|\/',expression)
    try:
        value = evaluate_expression(token)
        return value
    except ZeroDivisionError:
        return


def evaluate_expression(tokens):
    s = Stack()
    p = {')':'(','}':'{',']':'['}
    for i in tokens:
        try:
            i = int(i)
        except ValueError:
            pass
        if i not in p:
            s.push(i)
        else:
            try:
                arg2 = s.pop()
                operate = s.pop()
                arg1 = s.pop()
                symbol = s.pop()
                if symbol != p[i]:
                    return
                s.push({'+':add,'-':sub,'*':mul,'/':truediv}[operate](arg1,arg2))
            except EmptyStackError:
                return

    if s.is_empty():
        return
    value = s.pop()
    if s.is_empty():
        return value
    else:
        return



aaa = evaluate('({1 + (20 * 30)} - [400 / 500])')
print(aaa)