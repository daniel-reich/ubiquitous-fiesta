
def age_difference(ages):
  diff = sorted(ages)[-1] - sorted(ages)[-2]
  if diff == 1:
    return "1 year"
  elif diff > 1:
    return str(diff) + " years"
  else:
    return "No age difference between spouses."

