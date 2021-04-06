
def alpha_range(start, stop, step=1):
  if ord(start)>ord(stop) and step>0 or ord(start)<ord(stop) and step<0:
    start,stop = stop,start
  if start.islower() and stop.isupper() or start.isupper() and stop.islower():
    return 'both start and stop must share the same case'
  if abs(step)>=26 or step==0:
    return 'step must be a non-zero value between -26 and 26, exclusive'
  final = []
  for i in range(ord(start),ord(stop)-(1 if step<0 else -1),step):
    final.append(chr(i))
  return final

