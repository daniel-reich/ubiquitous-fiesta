
def bitwise_logical_negation(x):
  a = x | x >> 1
  a = a | a >> 2
  a = a | a >> 4
  return ~(a | a >> 8) & 1

