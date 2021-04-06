
def record_temps(records, currentWeek):
  res=[[z[1][0],z[0][1]] if z[1][0]<z[0][0] else [z[0][0],z[0][1]] \
  for z in zip(records,currentWeek)]
  return [[z[0][0],z[1][1]] if z[1][1]>z[0][1] else [z[0][0],z[0][1]] \
  for z in zip(res,currentWeek)]

