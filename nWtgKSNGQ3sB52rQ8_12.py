
def evenly_divisible(a, b, c):
    return sum([i if i%c == 0 else 0 for i in range(a,b+1)])

