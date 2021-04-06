
def record_temps(records, currentWeek):
  return [[min(r[0], c[0]), max(r[1], c[1])] for r, c in zip(records, currentWeek)]

