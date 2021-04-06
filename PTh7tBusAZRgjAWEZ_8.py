
def calc_diff(obj, limit):
  value_stolen = 0
  for item, value in obj.items():
    value_stolen += value
  return value_stolen - limit

