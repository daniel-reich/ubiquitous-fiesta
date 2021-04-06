
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  sa = [c for i,c in enumerate(str_A) if i not in ind_Z]
  sz = [c for i,c in enumerate(str_Z) if i not in ind_A]
  tot_a, tot_z = 0, 0
  for i in range(16):
    diff = ord(sa[i])-ord(sz[i])
    if diff > 0:
      tot_a += diff
    elif diff < 0:
      tot_z -= diff
  return {'A':tot_a,'Z':tot_z}

