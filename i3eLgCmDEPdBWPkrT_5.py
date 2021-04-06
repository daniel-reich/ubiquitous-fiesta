
def limit_number(num, range_low, range_high):
  if num>range_high:
    return range_high
  elif num<range_low:
    return range_low
  else:
    return num

