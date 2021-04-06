
def evenly_divisible(a, b, c):
    return sum([n for n in range(a,b+1) if n%c==0])

