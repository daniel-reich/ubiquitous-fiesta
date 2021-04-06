
def record_temps(records, currentWeek):
 result = []
 for i in range(len(records)):
  lst = []
  lst.append(min(records[i][0],currentWeek[i][0]))
  lst.append(max(records[i][1],currentWeek[i][1]))
  result.append(lst)
 return result

