
def min_turns(current, target):
    total = 0
    for i in range(len(current)):
        t = int(target[i])
        c = int(current[i])
        x = min(forward(t,c),backward(t,c))
        total += x
    return total
​
def forward(t,c):
    if c == t:
        return 0
    if c == 0:
        return t
    if c < t:
        return t - c
    if t == 0:
        return 10 - c
    if t < c:
        return (10 - c) + t
​
def backward(t,c):
    if c == t:
        return 0
    if c == 0:
        return 10 - t
    if c > t:
        return c - t
    if t == 0:
        return c
    if t > c:
        return (10 - t) + c

