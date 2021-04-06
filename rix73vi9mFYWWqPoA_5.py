
def record_temps(records, currentWeek):
  for i, t in enumerate(currentWeek):
    if t[0] < records[i][0]:
      records[i][0] = t[0]
    if t[1] > records[i][1]:
      records[i][1] = t[1]
  return records

