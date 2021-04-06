
def final(r,c,i):
    lst=[]
    row=[int(j[0]) for j in i if j[1]=='r']
    col=[int(j[0]) for j in i if j[1]=='c']
    for x in range(r):
        lst.append([])
        for y in range(c):
            lst[x].append(sum([1 if k==x else 0 for k in row]) + sum([1 if k==y else 0 for k in col]))
    return lst

