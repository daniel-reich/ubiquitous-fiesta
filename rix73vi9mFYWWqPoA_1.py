
def record_temps(r, c):
  return [[min(r[i][0],c[i][0]), max(r[i][1],c[i][1])] for i in range(7)]

