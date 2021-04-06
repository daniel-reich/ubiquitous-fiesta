
def numberSequence(n, odd=True, res=None):
    if res is None:
        if n < 1:
            return '-1'
        if n == 1:
            return '1'
        if n == 2:
            return '1 1'
        odd = n % 2
        if odd:
            n = (n + 1) // 2
        else:
            n //= 2
        res = '{}'.format(n)
        n -= 1
    if n > 1:
        res += ' {}'.format(n)
    elif n == 1:
        if odd:
            return res + ' 1 ' + res[::-1]
        else:
            return res + ' 1 1 ' + res[::-1]
    return numberSequence(n - 1, odd, res)

