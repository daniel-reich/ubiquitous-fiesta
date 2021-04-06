
def eval_algebra(eq):
    li = eq.split(' ')
    eq_pos, var_pos = li.index('='), li.index('x')
    if var_pos == 0 and eq_pos == 1:
        return eval(''.join(li[2:]))
    n = len(eq)
    if li[-1] == 'x' and li[-2] == '=':
        return eval(''.join(li[:eq_pos]))
    if var_pos > eq_pos:
        li = li[eq_pos + 1:] + ['='] + li[:eq_pos]
        eq_pos, var_pos = li.index('='), li.index('x')
    oper = li[1]
    if var_pos == 0:
        if oper == "+":
            return int(li[-1]) - int(li[2])
        else:
            return int(li[-1]) + int(li[2])
    else:
        if oper == "+":
            return int(li[-1]) - int(li[0])
        else:
            return -1*(int(li[-1]) - int(li[0]))

