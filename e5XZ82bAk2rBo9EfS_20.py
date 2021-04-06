
def clean_time(s):
  if s == 0:
    return '00'
  elif s < 10:
    return '0' + str(s)
  else:
    return str(s)
​
def bed_time(*times):
  ans = []
  for time in times:
    start = time[0]
    end = time[1]
    s_hour = start.split(":")[0]
    e_hour = end.split(":")[0]
    s_min = start.split(":")[1]
    e_min = end.split(":")[1]
    hour_diff = int(s_hour) - int(e_hour)
    min_diff = int(s_min) - int(e_min)
    if hour_diff < 0:
      hour_diff += 24
    if min_diff < 0:
      min_diff += 60
      hour_diff -= 1
    ans.append(clean_time(hour_diff) + ':' + clean_time(min_diff))
  return ans

