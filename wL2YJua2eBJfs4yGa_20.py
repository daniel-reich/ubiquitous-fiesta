
def babbage(n):
    i, len_n = int(pow(n, 0.5)), len(str(n))
    divisor = pow(10, len_n)
    while pow(i, 2) % divisor != n:
        i += 1
    return ('Babbage was {}correct!'.format(('in', '')[i == 99736])
            if n == 269696 else i)

