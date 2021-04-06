
def staircase(n):
    final=[]
    d=[]
    v=abs(n)
    for i in range(1,v+1):
        a=[]
        for j in range(v):
            while(len(a)<(v-i)):
                a.append("_")
                if len(a)==(v-i):
                    break
            while(len(a)<v):
                a.append("#")
                if len(a)==v:
                    break
        #a.append("\n")
        d.append("".join(a))
    if n<0:
        d=d[::-1]
    s=""
    for i in range(len(d)-1):
       s+=d[i]+"\n"
    s+=d[-1]
    return s

