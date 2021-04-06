
def repeated(s):
    
    for i in range(2,len(s)//2+1):
        if not len(s)%i==0: continue
        a=[]
        for j in range(len(s)//i):
            if s[i*j:i*j+i]==s[:i]: a.append(1)
            else:a.append(0)
        if sum(a)==len(a): return True    
    return False

