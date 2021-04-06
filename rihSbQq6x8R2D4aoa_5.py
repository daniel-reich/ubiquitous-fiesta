
def alpha_range(start, stop, step=1):
  if start.isupper() != stop.isupper():
    return 'both start and stop must share the same case'
  if step == 0 or step < -25 or step > 25:
    return "step must be a non-zero value between -26 and 26, exclusive"
  start,stop = ord(start),ord(stop)
  if step < 0:
    start,stop = max(start,stop),min(start,stop)-1
  else:
    start,stop = min(start,stop),max(start,stop)+1
  return [chr(i) for i in range(start,stop,step)]

