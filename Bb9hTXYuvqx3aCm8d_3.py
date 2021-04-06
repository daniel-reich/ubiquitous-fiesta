
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  str_A, str_Z, res_di = list(str_A), list(str_Z), {'A': 0, 'Z': 0}
  for num in ind_A:
    str_Z[num] = ''
  for num in ind_Z:
    str_A[num] = ''
  str_A, str_Z = ''.join(str_A), ''.join(str_Z)
  for a in range(16):
    if ord(str_A[a]) > ord(str_Z[a]): res_di['A'] += ord(str_A[a]) - ord(str_Z[a])
    elif ord(str_Z[a]) > ord(str_A[a]): res_di['Z'] += ord(str_Z[a]) - ord(str_A[a])
  return res_di

