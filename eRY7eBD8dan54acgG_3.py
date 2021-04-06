
def is_checkerboard(lst):
  return all(x[i] ^ x[i+1] for x in lst for i in range(len(x)-1))

