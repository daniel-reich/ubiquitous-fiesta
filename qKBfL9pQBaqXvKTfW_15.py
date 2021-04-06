
def sum_of_slices(l):
  z=[]
  a=0
  for e in l:
    if a+e>100:
      z+=a,
      a=0
    a+=e
  return z+[a]

