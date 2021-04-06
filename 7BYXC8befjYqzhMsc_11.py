
def classify_rug(pattern):
    p = pattern
    c = [1,1]
    for i in range(len(p)//2):
        if not p[i]==p[-i-1]:
            c[0]=0
            break
 
    for e in p:
        if c[1]==0:
            break
        for j in range(len(e)//2):
            if not e[j]==e[-j-1]:
                c[1]=0
                break
​
    if sum(c)==0:
        return "imperfect"
    elif sum(c)==1:
        if c[0]==1:
            return "horizontally symmetric"
        else:
            return "vertically symmetric"
    else:
        return "perfect"

