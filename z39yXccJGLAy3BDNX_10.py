
def flipping_bits(n):
    return int(''.join('0' if i=='1' else '1' for i in str(bin(n)[2:]).zfill(32)),2)

