
def last_dig(a, b, c):
    n1 = int(str(a)[-1])
    n2 = int(str(b)[-1])
    n3 = str(c)[-1]
    if str(n1*n2)[-1]==n3:
        return True
    else:
        return False

