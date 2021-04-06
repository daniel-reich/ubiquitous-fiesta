
def switches(n):
    i = 0
    while '{0:{1}b}'.format(i ^ (i >> 1), n) != n * '1':
        i += 1
    return i

