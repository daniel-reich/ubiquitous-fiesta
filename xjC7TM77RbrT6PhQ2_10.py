
def switches(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2**(n-1) + switches(n-2)

