
def eval_algebra(eq):
    lst = eq.split()
    if lst.index("x") == 4:
        if lst[1] == "+":
            return int(lst[0]) + int(lst[2])
        else:
            return int(lst[0]) - int(lst[2])
    if lst.index("x") == 2:
        if lst[1] == "+":
            return int(lst[4]) - int(lst[0])
        else:
            return int(lst[0]) - int(lst[4])
​
    if lst.index('x') == 0:
        if lst[1] == '+':
            return int(lst[4]) - int(lst[2])
        else:
            return int(lst[4]) + int(lst[2])

