
def staircase(n, c = 0):
    c += 1
    if n == 1 or n == -1:
        return "#" * c
    elif n < 0:
        return staircase((n + 1), c) +"\n" + "_" * (abs(n) - 1) + "#" * c 
    else:
        return "_" * (n - 1) + "#" * c +"\n" + staircase((n - 1), c)

