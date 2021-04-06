
def flipping_bits(n):
  s = ''.join(['0' if i == '1' else '1' for i in bin(n)[2:].zfill(32)])
  return int(s, 2)

