
def break_point(n):
    for i in range(len(str(n))):
        lft,rgt = str(n)[:i], str(n)[i:]
        if sum([int(x) for x in str(lft)]) == sum([int(x) for x in str(rgt)]):
            return True
    return False

