
def no_strangers(txt):
    txt = txt.lower().split()
    for x in range(len(txt)):
        for i in  '!?"",.':
            if i in txt[x]:
                txt[x] = txt[x].replace(i, "")
​
    dic = dict.fromkeys(set(txt), 0)
    acq, fri = [], []
    for x in txt:
        dic[x] += 1
        if dic[x] == 3:
            acq.append(x)
        if dic[x] == 5:
            fri.append(x)
            acq.remove(x)
    return [acq, fri]

