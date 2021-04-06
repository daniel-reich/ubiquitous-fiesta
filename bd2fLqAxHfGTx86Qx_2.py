
def can_complete(s, l):
    for i in s:
        f = l.find(i)
        if f == -1:
            return False
        l = l[f + 1:]
    return True

