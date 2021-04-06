
def widen_streets(lst, n):
    r = []
    s = ' '
    y = ''
    for item in lst:
        for item in item.split(' '):
            if item == '':
                y+=item.replace('', s*(n-1))
            else:
                y=(y+(s*n)+item).lstrip(' ')
       
        r.append(y)
        y = ''
    return r

