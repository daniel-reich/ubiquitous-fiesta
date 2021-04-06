
def age_difference(ages):
  ages.sort()
  diff = ages[-1]-ages[-2]
  if diff == 0:
    return "No age difference between spouses."
  elif diff ==1:
    return str(diff) + " year"
  else:
    return str(diff) + " years"

