
def max_possible(n1, n2):
    n1 = list(str(n1))
    n2 = list(reversed(sorted(list(str(n2)))))
    for i, x in enumerate(n1):
        if n2 and x<n2[0]:
            n1[i] = n2[0]
            del n2[0]
    return int(''.join(n1))

