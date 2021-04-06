
def generate_nonconsecutive(n):
    return ' '.join('{:0{}b}'.format(i, n) for i in range(int('1'*n, 2) + 1) if '11' not in bin(i))

