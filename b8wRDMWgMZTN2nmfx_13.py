
def equal(a, b, c):
    if [a,b,c].count(a) == 1 and [a,b,c].count(b) == 1:
        return 0
    elif [a,b,c].count(a)>=[a,b,c].count(b):
        return [a,b,c].count(a)
    else:
        return [a,b,c].count(b)

