
def pi(n):
    def atand(d,n):
        t=m=(10**n)//d
        i=0
        while m!=0:
            i+=1
            m//=-d*d
            t+=m//(2*i+1)
        return t
    d=n+5
    p=4*(4*atand(5,d)-atand(239,d))
    s=str(p)[:n+1]
    return s[0]+'.'+s[1:]

