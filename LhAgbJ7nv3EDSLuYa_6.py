
def golomb(n):
    if n==1:
        return [1]
    s=[0]*(n+1)
    s[1]=1
    s[2]=2
    k=1
    i=2
    j=2
    while j<n+1:
        if j-k==s[i]:
            s[j]=i
            k=j
            j+=1
            i+=1
        else :
            s[j]=i
            j+=1
    return s[1:]

