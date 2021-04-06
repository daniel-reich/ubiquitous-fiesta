
def initialize(names):
    s=[]
    xx=[]
    hh=[]
    for i in names:
        ii=i.split(" ")
        xx.append(ii)
    for x in xx:
        hh.append([z[0]+"."for z in x])
    for g in hh:
        s.append(" ".join(g))
    return s

