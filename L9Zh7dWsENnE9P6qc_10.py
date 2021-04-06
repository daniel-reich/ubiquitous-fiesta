
def josephus(people):
    a = list(range(1, people+1))
    k = 1
    while len(a) > 1:
        a.pop(k)
        k = (k+1) % len(a)
    return a[0]

