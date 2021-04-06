
def age_difference(ages):
  if sorted(ages)[-1]-sorted(ages)[-2]==0:
    return "No age difference between spouses."
  elif sorted(ages)[-1]-sorted(ages)[-2]==1:
    return "1 year"
  else:
    return "{} years".format(sorted(ages)[-1]-sorted(ages)[-2])

