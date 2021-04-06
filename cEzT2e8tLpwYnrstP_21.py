
def swap_d(k, v, swapped):
  if swapped: k, v = v, k
  return {a: b for a, b in zip(k, v)}

