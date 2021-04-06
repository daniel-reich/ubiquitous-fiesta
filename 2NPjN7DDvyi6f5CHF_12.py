
def age_difference(f_age, s_age):
  udif = 0
  ddif = 0
  ftemp = f_age
  stemp = s_age
  while True:
    if stemp*2==ftemp or s_age*2==f_age:
      break
    udif+=1
    ddif+=1
    s_age+=1
    f_age+=1
    ftemp-=1
    stemp-=1
  return min(udif,ddif)

