
def swap_d(k, v, swapped):
  if swapped == True:
    return {x: y for x, y in zip(v, k)}
  else:
    return {x: y for x, y in zip(k, v)}

