
def eval_algebra(eq):
    eq = eq.split()
    if eq[2] == 'x':
        if eq[1] == '+':
            return int(eq[-1]) - int(eq[0])
        else:
            return int(eq[0]) - int(eq[-1])
    elif eq[0] == 'x':
        if eq[1] == '+':
            return int(eq[-1]) - int(eq[2])
        else:
            return int(eq[2]) + int(eq[-1])
    elif eq[-1] == 'x':
        if eq[1] == '+':
            return int(eq[0]) + int(eq[2])
        else:
            return int(eq[0]) - int(eq[2])

