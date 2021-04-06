
def alpha_clash(str_a, ind_a, str_z, ind_z):
  a, s_a = 0, [ord(x) for i, x in enumerate(str_a) if i not in ind_z]
  z, s_z = 0, [ord(x) for i, x in enumerate(str_z) if i not in ind_a]
  for i, x in enumerate(s_a):
    if x > s_z[i]: a += x-s_z[i]
    else: z += s_z[i]-x
  return {'A': a, 'Z': z}

