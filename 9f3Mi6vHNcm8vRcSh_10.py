
def number_split(n):
    import math
    holding = []
    if n%2 == 0:
        a = int(n/2)
        holding.append(a)
        return holding*2
    else:
        b = math.floor(n/2)
        c = math.ceil(n/2)
        holding.append(b)
        holding.append(c)
        return holding

