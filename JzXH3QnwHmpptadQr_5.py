
def bitwise_logical_negation(x):
  return ((x >> 64) + 1) & ((~x + 1 >> 64) + 1)

