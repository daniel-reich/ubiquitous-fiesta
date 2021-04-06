
def record_temps(records, currentWeek):
  for i in range(7):
    records[i][0] = min(records[i][0], currentWeek[i][0])
    records[i][1] = max(records[i][1], currentWeek[i][1])
    
  return records

