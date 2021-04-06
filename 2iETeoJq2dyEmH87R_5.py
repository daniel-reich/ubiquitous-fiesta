
def count_digits(n, d):
    s = []
    for i in range(1,n+1):
        s.append(i**2)
    if d == 0:
        ctr = 1
    else: ctr = 0
    for i in s:
        ctr += str(i).count(str(d))
    return ctr

