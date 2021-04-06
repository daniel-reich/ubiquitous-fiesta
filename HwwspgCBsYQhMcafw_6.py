
def super_digit(n, k):
    a=0
    for i in range(len(n)):
        a+=int(n[i])
    s=str(a*k)
    while len(s)>1:
        a=0
        for i in range(len(s)):
            a+=int(s[i])
        s=str(a)
    return (int(s))

