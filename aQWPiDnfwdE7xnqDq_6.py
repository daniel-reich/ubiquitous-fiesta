
def drange(*args):
  start,end,diff = 0,1,1
  if len(args) == 3:
    start,end,diff = args
  elif len(args) == 2:
    start,end = args
  else:
    end = args[0]
  rnd = max(len(str(x).split('.')[1]) if '.' in str(x) else 0 for x in (start,end,diff))
  res = [start]
  while res[-1] + diff < end:
    res.append(round(res[-1]+diff,rnd))
  return tuple(res)

