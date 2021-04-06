
def look_and_say(s,n):
    r=[s]
    s=str(s)+'_'
    count=1
    while count<n:
        t=''
        p=0
        while p<len(s)-1:
            k=1
            while s[p]==s[p+1]:
                k+=1
                p+=1
            t+=str(k)+s[p]
            p+=1
        count+=1
        r.append(int(t))
        s=t+'_'
    return r

