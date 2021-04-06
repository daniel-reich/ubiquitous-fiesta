
def swap_d(k, v, swapped):
  dict = {}
  for index in range(0,len(k)):
    if swapped:
      dict[v[index]] = k[index]
    else:
      dict[k[index]] = v[index]
  return dict

