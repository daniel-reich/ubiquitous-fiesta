
def harry(po):
  if not po[0]: return -1
  n,m = len(po), len(po[0])
  for i in range(n-1):
    po[i+1][0]+= po[i][0]
  for j in range(m-1):
    po[0][j+1]+= po[0][j]
    for i in range(n-1):
      po[i+1][j+1]+= max(po[i+1][j], po[i][j+1])
  return po[n-1][m-1]

