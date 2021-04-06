
def max_possible(n1, n2):
    n1, n2 = list(str(n1)), sorted(list(str(n2)), reverse=True)
    for i in range(len(n1)):
        for j in range(len(n2)):
            try:
                if n2[j] > n1[i]:
                    n1[i] = n2[j]
                    n2.pop(j)
            except IndexError:
                pass
    return int(''.join(n1))

