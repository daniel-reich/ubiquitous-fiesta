
OP = {'+':int.__add__, '-':int.__sub__, '*':int.__mul__,
      '//': lambda a,b: a//b if b else -1 }
​
def arithmetic_operation(n):
    a, o, b = n.split()
    return OP[o](int(a), int(b))

