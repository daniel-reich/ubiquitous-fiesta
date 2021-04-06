
def ulam(n):
    ulist = [1, 2]
    sdict = {3: 1}
    if (n>=3):
        while len(ulist)<n:
            nou = min([k for k in sdict.keys() if sdict[k]==1])
            temp = [k for k in sdict.keys() if k<=nou]
            for k in temp:
                sdict.pop(k)
            temp = sdict.keys()
            for u in ulist:
                if (nou+u) in temp:
                    sdict[nou+u] = sdict[nou+u] + 1
                else:
                    sdict[nou+u] = 1
            ulist.append(nou)
    return ulist[n-1]

