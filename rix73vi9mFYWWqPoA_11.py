
def record_temps(records, currentWeek):
  for i in range(len(records)):
    currentWeek[i] += records[i];
  res = [];
  for i in currentWeek:
    res.append([min(i),max(i)]);
  return res;

