
def calc_diff(obj, limit):
  total = 0
  for price in obj.values():
    total += price
  return total - limit

