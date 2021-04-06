
def max_possible(n1, n2):
    n1 = [int(d) for d in str(n1)]
    n2 = sorted([int(d) for d in str(n2)], reverse=True)
    for i1, d1 in enumerate(n1):
        for i2, d2 in enumerate(n2):
            if d2 > d1:
                n1[i1] = n2.pop(i2)
                break
    return int(''.join(map(str, n1)))

