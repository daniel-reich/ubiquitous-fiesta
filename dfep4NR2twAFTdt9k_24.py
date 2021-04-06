
def matrix_mult(m1, m2):
  col = [[i[0] for i in m2],[i[1] for i in m2]]
  return [[prod(m1[0],col[i]) for i in range(2)],[prod(m1[1],col[i]) for i in range(2)]]
  
def prod(l1, l2):
  ans = 0
  for i in range(len(l1)):
    ans += l1[i]*l2[i]
  return ans

