
def id_mtrx(n):
    if not isinstance(n, int):
        return 'Error'
    if n > 0:
        return [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    else:
        return [[1 if j == abs(n) - i - 1 else 0 for j in range(abs(n))] for i in range(abs(n))]

