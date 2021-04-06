
def division(a, b):
    i = str(a//b)
    r = a % b
    rems = []
    dec = ''
    while r and r not in rems:
        rems.append(r)
        dec += str(10*r//b)
        r = (10*r) % b
    if not dec: dec='0'
    if r == 0:
        return "{}.{}".format(i,dec)
    idx = rems.index(r)
    return "{}.{}({})".format(i,dec[:idx],dec[idx:])

