
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  result = { 'A': 0, 'Z': 0 }
  arr_A = [str_A[i] for i in range(len(str_A)) if not i in ind_Z]
  arr_Z = [str_Z[i] for i in range(len(str_Z)) if not i in ind_A]
  for al, zl in zip(arr_A, arr_Z):
    score = ord(al) - ord(zl)
    if score > 0: 
      result['A'] += score
    else:
      result['Z'] -= score
  return result

