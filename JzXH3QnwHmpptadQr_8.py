
def bitwise_logical_negation(x):
  return ((x >> 31) | ((~x + 1) >> 31)) + 1

