
def limit_number(num, range_low, range_high):
  if num < range_low:
    return range_low
  elif num > range_high:
    return range_high
  else:
    return num

