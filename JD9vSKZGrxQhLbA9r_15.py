
def pile_of_cubes(m):
    total,n = 0,0
    while total<m:
        n+=1
        total += n**3
    return n if total==m else None

