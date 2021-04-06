
def mystery_func(txt):
  A=[x for x in txt if x.isalpha()]
  D=[int(x) for x in txt if x.isdigit()]
  s=''
  for i in range(len(A)):
    s+=A[i]*D[i]
  return s

