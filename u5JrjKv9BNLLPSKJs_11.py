
def num_ways(n, s):
    g = [0]*(n+1)
    j=0
    for i in range(n + 1):
        if i-j>0:    
            g[i] += sum(g[i - j] for j in s)
        if i in s:
            g[i]+=1
    return g[-1]

