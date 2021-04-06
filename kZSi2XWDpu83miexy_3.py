
OPER = {'+':int.__add__,'-':int.__sub__,'*':int.__mul__,'/':int.__floordiv__}
​
def post_fix(expr):
    oper = (n for n in expr.split() if n in '+-*/')
    a, *nums = (int(n) for n in expr.split() if n not in '+-*/')
    for o, b in zip(oper, nums):
        a = OPER[o](a, b)
    return a

