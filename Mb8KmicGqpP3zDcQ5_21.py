
def josephus(n, k):
    killed = []
    alive = list([True]*n)
    x, i = 0, 0
    while len(killed) < n:
        if alive[i]:
            x += 1
        if x == k:
            alive[i] = False
            killed.append(i+1)
            x = 0
        i += 1
        if i == n:
            i = 0
​
    return killed[-1]

