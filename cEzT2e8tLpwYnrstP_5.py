
def swap_d(k, v, swapped):
  if not swapped:
    new_dict_not_swapped = {}
    for i in range(len(k)):
      new_dict_not_swapped[k[i]] = v[i]
    return new_dict_not_swapped
  elif swapped:
    new_dict = {}
    for i in range(len(k)):
      new_dict[v[i]] = k[i]
    return new_dict

