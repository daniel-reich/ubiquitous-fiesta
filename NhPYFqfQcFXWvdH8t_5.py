
def egcd(j, k):
    if j == 0:
        return (k, 0, 1)
    h, y, x = egcd(k%j,j)
    return (h, x - (k//j) * y, y)
def mod_inv(j, m):
    h, x, y = egcd(j, m)
    if h != 1:
        return False
    return x%m

