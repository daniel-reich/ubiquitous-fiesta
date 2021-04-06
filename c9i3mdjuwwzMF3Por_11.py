
def P(n):
    if n==1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
def E(n):
    n=list(str(n))
    d={"6":"9", "9":"6"}
    for i in range(len(n)):
        if n[i] not in "01689":
            return False
        if n[i] in d:
            n[i]=d[n[i]]
    return P(int("".join(n)))
    
def bemirp(n):
    if P(n):
        if str(n)!=str(n)[::-1] and E(n):
            return "B"
        elif str(n)!=str(n)[::-1] and P(int(str(n)[::-1])) :
            return "E"
        else:
            return "P"
    else :
        return "C"

