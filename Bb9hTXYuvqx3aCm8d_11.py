
def delete_char(string, index):
  ans = ''
  for i in range(len(string)):
    if i not in index:
      ans += string[i]
  return ans
  
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  ans_A = delete_char(str_A, ind_Z)
  ans_Z = delete_char(str_Z, ind_A)
  z = 0
  a = 0
  for i in range(len(ans_A)):
    if ord(ans_A[i]) > ord(ans_Z[i]):
      a += ord(ans_A[i]) - ord(ans_Z[i])
    else:
      z += ord(ans_Z[i]) - ord(ans_A[i])
  return {'A': a, 'Z': z}

