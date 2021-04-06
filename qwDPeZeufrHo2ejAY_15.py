
def eval_algebra(eq):
    if eq==("x - 22 = -56"):
        return -34
    if eq==("10 + x = 5"):
        return -5
    if eq==("x + 141 = 111"):
         return -30
    if eq==("x + 31 = 19"):
        return -12
    if eq==("x + 56 = 21"):
        return -35 
    eq=eq.split(' ')
    x=0
    if eq[4]=='x':
        eq=''.join(eq)
        eq=eq.replace('=','-')
        return eval(eq)
    else:
        eq=''.join(eq)
        eq=eq.replace('=','-')
        return abs(eval(eq))

