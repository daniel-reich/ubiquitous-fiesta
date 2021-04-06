
def min_turns(current, target):
    final = []
    for x in range(4):
        i, j = 0, 0
        a, b = int(current[x]), int(current[x])
        while True:
            if b == int(target[x]) or a == int(target[x]):
                break
​
            a += 1
            i += 1
            if a == 10:
                a = 0
​
            b -= 1
            j += 1
            if b == -1:
                b = 9
​
        final.append(min([i, j]))
    return sum(final)

