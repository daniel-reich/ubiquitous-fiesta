
def simple_numbers(a, b):
    return [x for x in range(a, b+1) if simple(x)]
​
def simple(x):
    s = str(x)
    tot = 0
    for i, n in enumerate(s, start=1):
        tot += int(n) ** i
    return tot == x

