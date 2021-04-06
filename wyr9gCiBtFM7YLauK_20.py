
def time_sum(times):
  if times==[]: return [0,0,0]
  nums=[x.split(':') for x in times]
  sec=sum([int(x[-1]) for x in nums])
  min=sum([int(x[1]) for x in nums])+int(sec/60)
  hour=sum([int(x[0]) for x in nums])+int(min/60)
  return [hour,min%60,sec%60]

