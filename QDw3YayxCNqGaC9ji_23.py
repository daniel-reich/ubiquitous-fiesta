
def make_change(c):
    a=c//25
    b=c-a*25
    d=b//10
    e=b-d*10
    f=e//5
    g=e-f*5
    h={}
    h["q"]=a
    h["d"]=d
    h["n"]=f
    h["p"]=g
    return h

