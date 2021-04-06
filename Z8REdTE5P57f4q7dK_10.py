
def collatz(n):
    c=[]
    while n!=1:
        if n%2==0:
            a=n
            n=n/2
            c.append(a)
        else:
            a=n
            n=3*n+1
            c.append(a)
    return (len(c)+1,int(max(c)))

