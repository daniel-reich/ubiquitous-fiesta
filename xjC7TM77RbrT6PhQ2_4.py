
def switches(n):
    s=[1,2,0]
    if n<3:
        return s[n-1]
    for i in range(2,n):
        s[i]=s[i-1]+2*s[i-2]+1
        s.append(s[i])
    return s[n]

