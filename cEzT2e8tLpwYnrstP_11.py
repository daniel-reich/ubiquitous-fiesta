
def swap_d(k, v, swapped):
  return [{key: value for key, value in zip(k, v)}, {value: key for key, value in zip(k, v)}][swapped]

