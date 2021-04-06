
def record_temps(rec, cur):
  return [[min(rec[day][0],cur[day][0]), max(rec[day][1],cur[day][1])]
        for day in range(7)]

