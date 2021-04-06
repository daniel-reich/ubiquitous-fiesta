
def josephus(n, i):
    s=list(range(n))
    x=i-1
    while len(s)>1:
        s.pop(x)
        x=(x+(i-1))%(len(s))
    return s[0]+1

