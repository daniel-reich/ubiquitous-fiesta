
def swap_d(k, v, swapped):
  if swapped == False:
    return {i:j for i,j in zip(k,v)}
  else:
    return {j:i for i,j in zip(k,v)}

