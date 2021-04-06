
def age_difference(ages):
  ages.sort()
  diff = ages[-1]-ages[-2]
  return "{} year{}".format(diff, "s" if diff>1 else "") if diff else "No age difference between spouses."

