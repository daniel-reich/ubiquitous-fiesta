
def junction_or_self(n):
    Junction = [i for i in range(0, n+1) if i+sum([int(j) for j in str(i)])==n]
    if len(Junction)>0:
        return sorted(Junction, reverse=True)
    return "Self"

