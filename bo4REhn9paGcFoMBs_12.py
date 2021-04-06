
def age_difference(ages):
  x = abs(sorted(ages)[-2] - sorted(ages)[-1])
  if x == 0:
    return "No age difference between spouses."
  elif x == 1:
    return str(x) + ' year'
  return str(x) + ' years'

