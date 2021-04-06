
def matrix_mult(m1, m2):
  l=[]
  ml=[]
  l.append(m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0])
  l.append(m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1])
  ml.append(l)
  l=[]
  l.append(m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0])
  l.append(m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1])
  ml.append(l)
  return ml

