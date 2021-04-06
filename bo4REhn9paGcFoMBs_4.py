
def age_difference(ages):
  ages = sorted(ages)
  x = "No age difference between spouses."
  if ages[-1]-ages[-2]: x = str(ages[-1]-ages[-2]) + " year"
  if ages[-1]-ages[-2] > 1: x = str(ages[-1]-ages[-2]) + " years"
  return x

