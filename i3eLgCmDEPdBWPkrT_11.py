
def limit_number(num, range_low, range_high):
  return range_high if num > range_high else range_low if num < range_low else num

