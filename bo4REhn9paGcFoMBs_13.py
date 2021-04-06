
def age_difference(ages):
  i = sorted(ages)[-2:]
  if i[0] == i[1]: return "No age difference between spouses."
  else: 
    x = abs(i[0] - i[1])
    return "{} years".format(x) if x > 1 else "{} year".format(x)

