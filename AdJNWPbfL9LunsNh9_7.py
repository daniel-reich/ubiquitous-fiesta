
import copy
def multiplication_table(n):
    new = []; new1 = []; c = copy.copy(n)
    for i in range(1, n+1):
        for j in range(1, n ** 2 + 1):
            if j <= c and j % i == 0:
                if len(new) != n: new += [j]
        cu = copy.copy(new); new.clear()
        new1 += [cu]; c += c
    return new1

