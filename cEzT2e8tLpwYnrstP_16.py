
def swap_d(k, v, swapped):
  if swapped:
    k, v = v, k
  output = {k[i]:v[i] for i in range(len(k))}
  return output

