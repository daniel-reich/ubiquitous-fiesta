
def time_sum(times):
  lst = [x.split(':') for x in times]
  hrs = 0
  mn = 0
  sec = 0
  for l in lst:
    sec += int(l[2])
    mn += int(l[1])
    hrs += int(l[0]) 
  return [hrs+(mn+sec//60)//60, (mn+sec//60)%60, sec%60]

