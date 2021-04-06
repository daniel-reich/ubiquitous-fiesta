
def swap_d(k, v, swapped):
  if swapped == True:
    res = {v[i]: k[i] for i in range(len(v))}
  else:
    res = {k[i]: v[i] for i in range(len(k))}
  return res

