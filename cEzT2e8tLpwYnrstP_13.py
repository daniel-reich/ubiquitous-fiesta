
def swap_d(k, v, swapped):
  final_dct = {} 
  if swapped is False:
    for i in range(len(k)):
      final_dct.update({k[i]:v[i]})
  else:
    for i in range(len(k)):
      final_dct.update({v[i]:k[i]})
  return final_dct

