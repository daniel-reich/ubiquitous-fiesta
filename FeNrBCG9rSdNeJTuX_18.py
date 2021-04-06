
def max_possible(n1, n2):
  K1=[int(i) for i in str(n1)]
  K2=[int(i) for i in str(n2)]
  for i,n in enumerate(K1):
    if len(K2)<=0:
      break
    if n < max(K2):
      K1[i] = max(K2)
      K2.remove(K1[i])
  return int(''.join([str(i) for i in K1]))

