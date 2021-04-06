
def record_temps(rec, cw):
  return [[min(i[0], cw[idx][0]), max(i[1], cw[idx][1])] for idx, i in enumerate(rec)]

