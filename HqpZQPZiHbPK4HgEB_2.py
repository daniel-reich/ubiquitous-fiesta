
def maxmin(n):
    n = str(n)
    x = [(x,y) for x in range(len(n)) for y in range(len(n))]
    z = []
    for i in x:
        n0 = list(n)
        n0[i[0]], n0[i[1]] = n0[i[1]], n0[i[0]]
        z += [(''.join(n0))]
    z = [int(x) for x in z if x[0] != '0']
    return(max(z), min(z))

