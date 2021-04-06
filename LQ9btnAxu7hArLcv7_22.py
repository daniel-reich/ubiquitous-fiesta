
def diagonalize(n, d):
    if d == "ul":
        inc = (0, 0)
    elif d == "ur":
        inc = (0, -1)
    elif d == "ll":
        inc = (-1, 0)
    else:
        inc = (-1, -1)
    
    a = [[j + inc[1] + inc[0] for j in range(n * -inc[1] + i, n + n*inc[1] + i, inc[1]*2+1)] for i in range(n * -inc[0], n + n*inc[0], inc[0]*2+1)]
​
    return a

