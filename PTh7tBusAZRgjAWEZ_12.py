
def calc_diff(obj, limit):
  losses = 0
  for k in obj:
    losses += obj[k]
  return losses - limit

