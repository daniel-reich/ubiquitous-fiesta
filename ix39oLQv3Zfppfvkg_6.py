
def multiply_matrix(m1, m2):
  if len(m1[0])!=len(m2) or len(m1)!=len(m2[0]):
    return "ERROR"
  m2,m=list(map(list,zip(*m2))),[]
  for i in m1:
    sm=[]
    for j in m2:
      sm+=[sum(x*y for x,y in zip(i,j))]
    m+=[sm]
  return m

