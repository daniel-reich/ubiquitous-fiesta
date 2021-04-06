
import operator
​
def arithmetic_operation(n):
    exp = n.split()
    a, op, b = int(exp[0]), exp[1], int(exp[2])
    try:
        ops = {'+': operator.add(a, b),
              '-' : operator.sub(a, b),
               '*': operator.mul(a,b),
               '//' : operator.floordiv(a, b)
              }
    except ZeroDivisionError:
        return -1
    return ops[op]

