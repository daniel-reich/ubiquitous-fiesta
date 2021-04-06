
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  ind_A = sorted(ind_A, reverse=True)
  ind_Z = sorted(ind_Z, reverse=True)
  for i in ind_A: str_Z = str_Z[:i] + str_Z[i+1:]
  for i in ind_Z: str_A = str_A[:i] + str_A[i+1:]
  s = {'A': 0, 'Z': 0}
  for i in range(16):
    x = ord(str_A[i]) - ord(str_Z[i])
    if x > 0:
      s['A'] += x
    else:
      s['Z'] -= x
  return s

