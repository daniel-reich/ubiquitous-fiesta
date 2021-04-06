
def record_temps(records, currentWeek):
  i = 0
  for day in currentWeek:
    for temp in day:
      if temp < records[i][0] : records[i][0] = temp
      elif temp > records[i][1] : records[i][1] = temp
    i += 1
  return records

