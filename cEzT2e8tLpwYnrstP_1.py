
def swap_d(k, v, swapped):
  if swapped:
    k,v = v,k
  return dict(zip(k,v))

