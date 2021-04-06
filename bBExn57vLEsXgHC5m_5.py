
def same_line(lst):
  k0=lst[0]
  k1=lst[1]
  k2=lst[2]
  g1=(k1[1]-k0[1])*(k2[0]-k1[0])
  g2=(k2[1]-k1[1])*(k1[0]-k0[0])
  return (g1==g2)

