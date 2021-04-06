
def kempner(n,i=1,t=1):
    if t%n==0: return max(1,i-1)
    return kempner(n,i+1,t*i)

