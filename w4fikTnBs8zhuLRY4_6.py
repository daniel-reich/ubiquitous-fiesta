
def rep_set(n):
    if n == 0:
        return []
    if n == 1:
        return [[]]
    return [rep_set(i) for i in range(n)]

