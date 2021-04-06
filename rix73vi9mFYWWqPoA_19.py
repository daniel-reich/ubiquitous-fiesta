
def record_temps(r, cw):
  for i in range(len(r)):
    if cw[i][0]<r[i][0]: r[i][0]=cw[i][0]
    if cw[i][1]>r[i][1]: r[i][1]=cw[i][1]
  return r

