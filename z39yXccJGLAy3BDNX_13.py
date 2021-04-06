
def flipping_bits(n):
  x = bin(n)
  y = ''.join(['1' if y == '0' else '0' for y in x[2:].zfill(32)])
  return int(y,2)

