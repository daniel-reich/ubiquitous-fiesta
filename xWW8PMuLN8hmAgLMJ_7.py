
def postfix(expression):
    lst = expression.split()
    idx = 0
    while True:
        if str(lst[idx]) in "+-/*":
            a = eval(str(lst[idx - 2]) + ' ' + lst[idx] + ' ' + str(lst[idx - 1]))
            lst[idx-2] = a
            lst.pop(idx)
            lst.pop(idx - 1)
            if len(lst) == 1: return lst[0]
            idx -= 2
        else:
            idx += 1

