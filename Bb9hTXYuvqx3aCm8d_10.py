
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  for i in ind_Z:
    str_A = str_A.replace(str_A[i],' ')
  str_A = ''.join(str_A.split(' '))
  for i in ind_A:
    str_Z = str_Z.replace(str_Z[i],' ')
  str_Z = ''.join(str_Z.split(' '))
  A,Z = 0,0
  for i in zip([i for i in str_A],[i for i in str_Z]):
    (x,y) = i
    if ord(x) > ord(y):
      A += ord(x) - ord(y)
    else:
      Z += ord(y) - ord(x)
  return {'A':A,'Z':Z }

