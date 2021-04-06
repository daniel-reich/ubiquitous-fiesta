
def num_split(n):
    lt=[]
    if n<0:
        n=str(n).lstrip("-")
        for x in range(len(str(n))):
            a=int(n)%10
            lt.append(-a*(10**x))
            n=int(n)//10
    else:
        for x in range(len(str(n))):
            a=n%10
            lt.append(a*(10**x))
            n=n//10
    return lt[::-1]

