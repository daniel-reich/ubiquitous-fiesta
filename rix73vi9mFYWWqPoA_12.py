
def record_temps(rec, week):
  return [sorted(week[i] + rec[i])[::3]  for i in range(len(rec))]

