
def pile_of_cubes(n):
    total=0
    f=0
    while (total<n):
        f+=1
        total+=(f**3)
    return f if total==n else None

