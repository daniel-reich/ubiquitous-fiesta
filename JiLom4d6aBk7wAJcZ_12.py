
def is_sastry(n):
    import math
    x = math.sqrt(int(str(n) + str(n+1)))
    return int(x)**2 == int(str(n) + str(n+1))

