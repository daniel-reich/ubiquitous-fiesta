
def time_sum(times):
  a = [x.split(':') for x in times]
  if len(times)==0: return [0, 0, 0]
  else: b = [[int(x) for x in y] for y in a ]
  i=0
  c=0
  d=0
  e=0
  while i<len(b):
    c+=b[i][0]
    d+=b[i][1]
    e+=b[i][2]
    i+=1
  c = c+(d//60)
  d = d%60+(e//60)
  e=e%60
  return [c, d, e]

