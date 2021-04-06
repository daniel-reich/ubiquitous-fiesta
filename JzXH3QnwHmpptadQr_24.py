
def bitwise_logical_negation(x):
  return ((~(x & ((~x) + 1)) + 1) >> 31) & 1 ^ 1

