
def calc_diff(obj, limit):
  plus = 0
  for x in obj.values():
    plus += x
  return plus - limit

