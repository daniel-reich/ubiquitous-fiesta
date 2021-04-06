
import operator
def arithmetic_operation(n):
    lst = n.split(" ")
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv}
    x, o, y = int(lst[0]), ops[lst[1]], int(lst[-1])
    try:
        return o(x, y)
    except ZeroDivisionError:
        return -1

