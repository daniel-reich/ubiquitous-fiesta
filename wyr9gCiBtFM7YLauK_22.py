
def time_sum(times):
  total = [0,0,0]
  for i in times:
    j=i.split(':')    
    for i in range(3):
      total[i]+=int(j[i])
  for i in reversed(range(2)):
    total[i]+=total[i+1]//60
    total[i+1]%=60
  return total

