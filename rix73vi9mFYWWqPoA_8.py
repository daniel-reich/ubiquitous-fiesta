
def record_temps(records, currentWeek):
  res = []
  for i in range(len(records)):
    min_temp = records[i][0]
    max_temp = records[i][1]
    if currentWeek[i][0] < records[i][0]:
      min_temp = currentWeek[i][0]
    if currentWeek[i][1] > records[i][1]:
      max_temp = currentWeek[i][1]
    res.append([min_temp, max_temp])
  return res

