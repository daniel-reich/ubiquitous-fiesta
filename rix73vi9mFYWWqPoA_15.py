
def record_temps(records, currentWeek):
  return [[min(records[i][0],currentWeek[i][0]),max(records[i][1],currentWeek[i][1])] for i in range(len(records))]

