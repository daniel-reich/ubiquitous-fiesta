
def is_economical(n):
    i = 2
    a = n
    factDict = {}
    while a > 1:
        if a % i == 0:
            if i not in factDict:
                factDict[i] = 1
            else:
                factDict[i] += 1
            a = a // i
        else:
            i += 1
    ctr = 0
    for k,v in factDict.items():
        ctr += len(str(k))
        if v != 1:
            ctr += len(str(v))
               
    if len(str(n)) > ctr:
        return 'Frugal'
    elif len(str(n)) == ctr:
        return 'Equidigital'
    else:
        return 'Wasteful'

