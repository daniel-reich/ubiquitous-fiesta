
def id_mtrx(n):
    if not type(n) == int: return 'Error'
    s = 1 if n >= 0 else -1
    return [[1 if i == j else 0 for i in range(abs(n))] 
            for j in range(abs(n))][::s]

