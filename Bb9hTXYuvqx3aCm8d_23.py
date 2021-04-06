
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  a = list(str_A)
  orda = []
  z = list(str_Z)
  ordz = []
  acopy = a.copy()
  zcopy = z.copy()
  apoints = 0
  zpoints = 0
  for i in ind_Z:
    a.remove(acopy[i])
  print(a)
  for i in ind_A:
    z.remove(zcopy[i])
  print(z)
  for i in a:
    orda.append(ord(i))
  for i in z:
    ordz.append(ord(i))
  for i in range(len(ordz)):
    if orda[i]>ordz[i]:
      apoints+=(orda[i]-ordz[i])
    elif orda[i]<ordz[i]:
      zpoints+=(ordz[i]-orda[i])
  return {"A":apoints,"Z":zpoints}

