
def swap_d(k, v, swapped):
  dictionary = {}
  for each in range(len(k)): # Range doesn't matter. Can be keys or values.
    if swapped:
      dictionary.update({v[each] : k[each]})
    else:
      dictionary.update({k[each] : v[each]})
  return dictionary

