
def swap_d(k, v, swapped):
  if swapped == False:
    x = dict(zip(k, v))
    return x
  else:
    x = dict(zip(v, k))
    return x

