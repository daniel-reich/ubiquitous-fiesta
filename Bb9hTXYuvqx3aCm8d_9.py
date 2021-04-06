
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  A = [ord(c) for i, c in enumerate(str_A) if i not in ind_Z]
  Z = [ord(c) for i, c in enumerate(str_Z) if i not in ind_A]
  s_A = sum(max(av - zv, 0) for av, zv in zip(A,Z))
  s_Z = sum(max(zv - av, 0) for av, zv in zip(A,Z))
  return {"A":s_A, "Z":s_Z}

