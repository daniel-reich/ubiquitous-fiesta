
def hex_lattice(size):
    n = int(((size-1)/3)**0.5)
    if 1+3*(n+1)*n != size:
        return 'Invalid'
    fmt = '{:^%d}' % (n*4+3)
    return '\n'.join((fmt.format(' '.join('o'*os))
            for os in (n*2+1-abs(n-i) for i in range(n*2+1))))

