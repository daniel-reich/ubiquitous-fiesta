
def time_sum(times):
  seconds = 0
  for t in times:
    tParts = [int(i) for i in t.split(':')]
    seconds += tParts[0]*60*60 + tParts[1]*60 + tParts[2]
  
  min, sec = divmod(seconds, 60)
  hours, min = divmod(min, 60)
  return [hours, min, sec]

