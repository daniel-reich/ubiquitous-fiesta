
def record_temps(r, cW):
  return [[min(j[0], cW[i][0]), max(j[1], cW[i][1])] for i, j in enumerate(r)]

