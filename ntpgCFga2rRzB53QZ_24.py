
def staircase(n):    
    a=[]
    if n>0:
        for i in range(0,n): a.append((n-1-i)*"_"+(i+1)*"#")    
    elif n<0:
        for i in range(abs(n)): a.append((i*"_")+(abs(n)-i)*"#")
    return "\n".join(a)

