
abbreviate = lambda s, n=4: ''.join(x[0].upper() for x in s.split(' ') if len(x) >= n)

