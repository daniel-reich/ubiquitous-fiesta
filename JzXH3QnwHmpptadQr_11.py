
def bitwise_logical_negation(x):
  x = ~x 
  x = x & (x >> 8) & 0xFF
  x = x & (x >> 4) & 0xF
  x = x & (x >> 2) & 0x3
  x = x & (x >> 1) & 0x1
  return x

