
def iterator(lst):
    if len(lst)==0:
        return 0
    for i in lst:
        return 1+iterator(i)
    
def func(lst):
    ele=0
    for i in lst:
        for j in i:
            if not (isinstance(j, list)):
                ele+=len(i)
                break
            else:
                ele+=iterator(i)
    return len(lst)+ele

