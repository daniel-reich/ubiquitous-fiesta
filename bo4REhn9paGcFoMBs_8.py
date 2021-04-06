
def age_difference(ages):
  diff = sorted(ages)[-1] - sorted(ages)[-2]
  if 1 < diff < 18:
    return '{} years'.format(diff)
  elif diff == 1:
    return '{} year'.format(diff)
  else:
    return "No age difference between spouses."

