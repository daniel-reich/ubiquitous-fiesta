
def limit_number(num, range_low, range_high):
  if range_low < num < range_high:
    return num
  elif num > range_high:
    return range_high
  else:
    return range_low

