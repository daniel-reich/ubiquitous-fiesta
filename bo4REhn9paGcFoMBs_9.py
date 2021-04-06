
def age_difference(ages):
  ages = sorted(ages)
  diff = ages[-1] - ages[-2]
  
  if diff == 0:
    return 'No age difference between spouses.'
  elif diff == 1:
    return '{} year'.format(diff)
  else:
    return '{} years'.format(diff)

