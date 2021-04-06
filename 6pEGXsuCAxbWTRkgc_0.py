
def loves_me(n):
    arr = (['Loves me', 'Loves me not']*n)[:n]
    arr[-1] = arr[-1].upper()
    return ', '.join(arr)

