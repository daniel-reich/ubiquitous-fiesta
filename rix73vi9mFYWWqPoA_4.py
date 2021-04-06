
def record_temps(records, currentWeek):
  return [[min(d[0], records[i][0]), max(d[1], records[i][1])] for
      i, d in enumerate(currentWeek)]

