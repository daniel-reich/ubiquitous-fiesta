
def eval_algebra(eq):
    a, b, c, d, e = eq.split()
    if e=="x":
        return eval(a+b+c)
    elif a=="x":
        return int(e) - int(c) if b=="+" else int(e)+int(c)
    elif c=="x":
        return int(e)-int(a) if b=="+" else int(a)-int(e)

