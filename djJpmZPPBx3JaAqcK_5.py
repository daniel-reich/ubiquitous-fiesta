
def maya_number(n):
    if n == 0:
        lod = [0]
    else:
        lod = []
        while n:
            lod = [n%20] + lod
            n = n // 20
    return [f(x) for x in lod]
​
def f(x):
    r = x % 5
    q = x // 5
    if x == 0:
        return '@'
    s = ''
    s += r * 'o' 
    s += q * '-'
    return s

