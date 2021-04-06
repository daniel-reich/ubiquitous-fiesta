
def count_ones(lst): #w/o built-in
    def l(it):
        c = 0
        while it:
            c += 1
            it = it[1:]
        return c
    d = {0: "0", 1: "1"}
    st = ""
    for i in lst:
        st += d[i]
    s, tmp = [], ""
    for i in st:
        if i == "0":
            s += [tmp]
            tmp = ""
        else:
            tmp += i
    if tmp:
        s += [tmp]
    count = 0
    for x in s:
        if l(x) > 1:
            count += 1
    return count

