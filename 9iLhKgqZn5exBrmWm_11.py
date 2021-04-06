
def ascending(txt):
    res =[]
    for i in range(1,len(txt)):
        if len(txt) % i == 0:
            tmp = []
            for j in range(len(txt) // i) :
                tmp.append(int(txt[j*i:(j+1) *i]))
            res.append(tmp)
    for i in res:
        c = True
        for n in range(1, len(i)) :
            if not i[n -1] + 1 == i[n]:
                c = False
        if c:
            return True
    return False

