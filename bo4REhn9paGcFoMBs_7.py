
def age_difference(ages):
  d = [max(ages)-i for i in ages]
  if d.count(0)==2:
    return "No age difference between spouses."
  d = min([i for i in d if i!=0])
  return str(d)+' years' if d>1 else '1 year'

