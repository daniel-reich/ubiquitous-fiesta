
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  lst_A, lst_Z = list(str_A), list(str_Z)
  ind_A, ind_Z = sorted(ind_A, reverse=True), sorted(ind_Z, reverse=True)
  for ndx_A, ndx_Z in zip(ind_A, ind_Z):
    lst_A.pop(ndx_Z)
    lst_Z.pop(ndx_A)
  
  A, Z = 0, 0
  for a, z in zip(lst_A, lst_Z):
    p = ord(a)-ord(z)
    if p > 0:
      A += p
    else:
      Z += -1 * p
  return {'A':A, 'Z':Z}

