
def flipping_bits(n):
    binary = '{0:b}'.format(n)
    flipped = ''.join(['1' if x == '0' else '0'
         for x in binary.zfill(32)])
    return int(flipped, 2)

