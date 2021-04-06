
def jazzify(lst):
    l=[]
    for i in lst:
        if i[-1] not in '7':
            l.append(i+'7')
        else:
            l.append(i)
    return l

