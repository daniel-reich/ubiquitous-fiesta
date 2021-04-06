
def eval_algebra(eq):
    eq = eq.split()
    if eq[4] == 'x':
        if eq[1] == '+':
            return int(eq[0]) + int(eq[2])
        else:
            return int(eq[0]) - int(eq[2])
    if eq[0] == 'x':
        if eq[1] == '+':
            return int(eq[4]) - int(eq[2])
        else:
            return int(eq[4]) + int(eq[2])
    if eq[2] == 'x':
        if eq[1] == '+':
            return int(eq[4]) - int(eq[0])
        else:
            return int(eq[0]) - int(eq[4])

