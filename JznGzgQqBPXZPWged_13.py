
def se(lst):
    s = 0
    for i in lst:
        s+=i
    return s
def par(lst):
    s = 0
    for i in lst:
        if i !=0:
            s+=1/i
    return round((1/s),1)
def Mod(net):
    r = ""
    for e in net:
        if e=="(":
            r+= "se(["
        elif e==")":
            r+= "])"
        elif e=="[":
            r+="par(["
        elif e=="]":
            r+="])"
        else:
            r+=e
    return r
def resist(net):
    m_net = Mod(net)
    return eval(m_net)

