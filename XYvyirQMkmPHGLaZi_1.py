
def boom_intensity(n):
    if n < 2:
        return 'boom'
    s = 'B{}m'.format('o'*n)
    if not n%2:
        s += '!'
    if not n%5:
        s = s.upper()
    return s

