
def calc_diff(obj, limit):
  keys = list(obj.keys())
  total = 0
  for each in keys:
      total += obj[each]
  return total-limit

