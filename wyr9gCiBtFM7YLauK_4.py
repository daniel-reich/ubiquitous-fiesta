
def time_sum(times):
  hSum = 0
  mSum = 0
  sSum = 0
  tiempos = []
  for time in times:
    tiempos = time.split(':')
    sSum+=int(tiempos[2])
    if sSum>60:
      mSum+=1
      sSum=sSum%60
    mSum+=int(tiempos[1])
    if mSum>60:
      hSum+=1
      mSum=mSum%60
    hSum+=int(tiempos[0])
  return [hSum, mSum, sSum]

