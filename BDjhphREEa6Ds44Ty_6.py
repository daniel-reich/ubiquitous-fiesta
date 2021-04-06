
def bomb(lst):
  p1,p2,t1 = lst[0]
  q1,q2,t2 = lst[1]
  r1,r2,t3 = lst[2]
  if t1 == 0: return (p1,p2)
  mat = [[2*(q1-p1), 2*(q2-p2), (0.343*t1)**2 - (0.343*t2)**2-p1**2 -p2**2+q1**2+q2**2]]
  mat += [[2*(r1-p1), 2*(r2-p2), (0.343*t1)**2 - (0.343*t3)**2-p1**2-p2**2+r1**2+r2**2]]
  x = (mat[0][2]*mat[1][1]-mat[1][2]*mat[0][1])/(mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1])
  y =-(mat[0][2]*mat[1][0]-mat[1][2]*mat[0][0])/(mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1])
  return (round(x,1),round(y,1))

