
def golomb(n):
    g, x = [1,2,2], 3
    while len(g)<n:
        g.extend([x]*g[x-1])
        x+=1
    return g[:n]

