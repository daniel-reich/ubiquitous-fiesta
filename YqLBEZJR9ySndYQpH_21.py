
def staircase(s):
    g = ''
    r = s
    if str(s)[0] != '-':
        for i in range(1, (s + 1)):
            r -= 1
            if i != s:
                g = g + ('_'*r) + ('#'*i) + '\n'
            else:
                g = g + ('_'*r) + ('#'*i)
        return g
    else:
        s = int(str(s).replace('-', ''))
        r = s
        for i in range(s):
            if i != (s - 1):
                g = g + ('_'*i) + ('#'*r) + '\n'
            else:
                g = g + ('_'*i) + ('#'*r)
            r -= 1
        return g

