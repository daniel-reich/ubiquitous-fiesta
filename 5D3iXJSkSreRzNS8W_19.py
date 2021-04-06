
def news_at_ten(txt, n):    
    a=[]
    
    if len(txt) >= n:
        for i in range(n):
            a.append(" "*(n-i)+txt[:i])
        for i in range(len(txt) - n+1):
            a.append(txt[i:n+i])
        for i in range(1,n):
            a.append(txt[-n+i:]+" "*i)
    else:
        for i in range(len(txt)+1):
            a.append(" "*(n-i)+txt[:i])
        for i in range(1, n-len(txt)+1):
            a.append(" "*(n-len(txt)-i)+ txt + " "*i)
        for i in range(1,len(txt)):
            a.append(txt[i:]+" "*(n-len(txt)+i))
    a.append(" "*n)
    return (a)

