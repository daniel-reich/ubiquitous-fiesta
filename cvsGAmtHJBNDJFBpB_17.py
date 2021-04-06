
def can_traverse(x):
    t = list(zip(*x))
    h = [f(r) for r in t]
    return len([1 for i in range(1, len(h)) if abs(h[i] - h[i-1]) > 1]) == 0
​
def f(r):
    for i in range(len(r)):
        if r[i] == 1:
            return i
    return len(r)

