
def flipping_bits(n):
  n = ('0' * (32 - len(bin(n)[2:]))) + bin(n)[2:]
  return int(''.join('1' if i=='0' else '0' for i in n), 2)

