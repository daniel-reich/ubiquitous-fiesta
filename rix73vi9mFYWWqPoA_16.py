
def record_temps(records, currentWeek):
  nr = []
  for i in range(len(records)):
    day = records[i]
    if currentWeek[i][0] < day[0]:
      day[0] = currentWeek[i][0]
    if currentWeek[i][1] > day[1]:
      day[1] = currentWeek[i][1]
    nr.append(day)
  return nr

