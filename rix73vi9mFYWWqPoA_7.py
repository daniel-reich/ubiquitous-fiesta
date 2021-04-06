
def record_temps(records, currentWeek):
  res = []
  for i, j in zip(records, currentWeek):
    res.append([min(i+j)] + [max(i+j)])
  
  return res

