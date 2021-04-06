
def is_early_bird(_range, n):
    s=[]
    n=str(n)
    diff=[]
    for i in range(0,_range+1):
        s.append(str(i))
    s=''.join(s)
    for i in range(len(s)-len(n)+1):
        d=[]
        for j in range(len(n)):
            if s[i+j]==n[j]:
                d.append(i)
        if len(d)==len(n):
            diff.append(d)
    for i in range(len(diff)):
        for j in range(len(diff[i])):
            x=i-i
            diff[i][j]=diff[i][j]+x+j
    if len(diff)==1:
        return diff
    else:
        diff.append("Early Bird!")
        return diff

