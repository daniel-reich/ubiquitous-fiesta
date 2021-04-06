
def loves_me(n):
    lver = 'Loves me, '
    for i in range(1, n):
        if (i % 2) == 0:
            lver += 'Loves me, '
        else:
            lver += 'Loves me not, '
    lver = lver.split(',')
    del lver[n]
    lver[n-1] = lver[n-1].upper()
    new = ','.join(lver)
    return new

