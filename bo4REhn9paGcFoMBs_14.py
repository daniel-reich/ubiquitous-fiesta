
def age_difference(ages):
  a = sorted(ages)
  y = a[-1] - a[-2]
  return "No age difference between spouses." if y ==0 else str(y) + ' year' + 's'*(y>1)

