
def XOR(a, b):
  x = a ^ b
  a = x ^ a
  b = x ^ b
  return [a, b]

