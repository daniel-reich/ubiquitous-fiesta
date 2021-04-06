
def time_sum(times):
  result = [0,0,0]
  for time in times:
    temp = time.split(":")
    for i in range(3):
      result[i] += int(temp[i]) 
  print (result)
  extra_minutes = int(result[2] / 60)
  result[2] = int(result[2] % 60)
  extra_hours = int((result[1] + extra_minutes) / 60)
  result[1] = (result[1] + extra_minutes) % 60
  result[0] += extra_hours
  return result

