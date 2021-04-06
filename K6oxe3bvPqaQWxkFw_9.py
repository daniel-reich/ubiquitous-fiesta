
def join_digits(n):
    s = ''.join((str(i)for i in range(1, n+1)))
    return '-'.join((i for i in s))

