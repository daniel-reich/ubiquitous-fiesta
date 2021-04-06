
def can_build(s1, s2):
    lst = list(s1)
    for i in list(s2):
        if i in lst:
            lst.remove(i)
        else:
            return(False)
    return(True)

