
def track_robot(*steps):
  p = [0,0]
  for i,s in enumerate(steps): p[i%2==0] += s * [-1,1][i%4<2]
  return p

