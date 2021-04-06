
def repeated(s):
    return len([i for i in range(1,len(s)//2+1) if s[0:i]*(len(s)//i)==s])>0

