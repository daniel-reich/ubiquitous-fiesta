
def collatz(n):
    nl=[]
    n=n
    nl.append(n)
    while n != 1:
        if n%2!=0:
            n=n*3+1
            nl.append(n)
        elif n != 1 and n%2==0:
            n=n//2
            nl.append(n)
    return (len(nl),max(nl))

