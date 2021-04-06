
def flipping_bits(n):
  a = bin(n)[2:]
  a = '0'*(32-len(a)) + a
  a = ''.join([['1','0'][int(i)] for i in a])
  return int(a,2)

