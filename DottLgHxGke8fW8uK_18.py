
def nPr(n, r):
    end, sol = n-r, 1
    while n > end: sol *= n; n -= 1
    return sol
​
def nCr(n, r):
    e, s, sol = min(r, n-r), 1, 1
    while s < e+1: sol = (sol*n)//s; n -= 1; s += 1
    return sol

