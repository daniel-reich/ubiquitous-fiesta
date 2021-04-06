
def limit_number(num, range_low, range_high):
  if num >= range_low and num <= range_high:
    return num
  while num < range_low:
    return range_low
  else:
    return range_high

