
def sub_freq(lst, num, level=0):
    fdict = dict()
    fdict[level] = fdict.get(level, 0) 
    for a in lst:
        if type(a)==list:
            ndict = sub_freq(a, num, level+1)
            for a in ndict:
                fdict[a] = fdict.get(a, 0) + ndict[a]
        elif a == num:
            fdict[level] += 1
    return fdict
​
def freq_count(lst, num):
    ndict = sub_freq(lst, num)
    flst = list()
    for a,b in ndict.items():
        flst.append([a,b])
    return sorted(flst, key=lambda x: x[0])

