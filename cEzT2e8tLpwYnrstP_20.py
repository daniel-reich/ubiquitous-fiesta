
def swap_d(k, v, swapped):
  return { v[i] : k[i] for i in range(len(k)) } if swapped else { k[i] : v[i] for i in range(len(k)) }

