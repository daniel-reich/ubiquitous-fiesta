
def time_adjust(now, hrs, mins, sec):
  
  now = now.split(':')
  
  nowhrs = int(now[0])
  nowmins = int(now[1])
  nowsecs = int(now[2])
  
  nowsecs += sec
  stopcount = 0
  while nowsecs >= 60 and stopcount < 1000:
    nowmins += int(nowsecs / 60)
    nowsecs = int(nowsecs % 60)
    stopcount += 1
  
  stopcount = 0
  nowmins += mins
​
  while nowmins >= 60 and stopcount < 10000:
    nowhrs += 1
    nowmins -= 60
    stopcount += 1
  
  stopcount = 0
  nowhrs += hrs
  while nowhrs >= 24 and stopcount < 1000:
    nowhrs -= 24
    stopcount += 1
  
  nowhrs = str(nowhrs)
  nowmins = str(nowmins)
  nowsecs = str(nowsecs)
  
  if len(nowhrs) < 2:
    nowhrs = '0' + nowhrs
  if len(nowmins) < 2:
    nowmins = '0' + nowmins
  if len(nowsecs) < 2:
    nowsecs = '0' + nowsecs
    
  return ':'.join([nowhrs, nowmins, nowsecs])

