
def arithmetic_progression(start, diff, n):
    a = [str(start)]
    b = start
    for i in range(n-1):
        b += diff
        a.append(str(b))
​
    return ', '.join(a)

