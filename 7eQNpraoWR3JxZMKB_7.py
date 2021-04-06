
def my_sub(a, b):
  return b if a == 0 else my_sub((~b & a) << 1, a ^ b)

