
def calc_diff(obj, limit):
  sum_of_values = 0
  for i in obj.values():
    sum_of_values += i
  return sum_of_values - limit

