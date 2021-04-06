
def age_difference(ages):
  sp = sorted(ages, reverse=True)[:2]
  dif = abs(sp[0]-sp[1])
  d = {0:"No age difference between spouses.",1:"1 year"}
  return d.get(dif,str(dif)+" years")

