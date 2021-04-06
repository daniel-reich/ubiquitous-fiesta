
def limit_number(num, range_low, range_high):
  if range_low < num < range_high:
    return num
  elif num < range_low:
    return range_low
  else:
    return range_high

