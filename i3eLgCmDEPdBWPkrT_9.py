
def limit_number(num, range_low, range_high):
  if range_low<=num<= range_high:
      return num
  elif num<range_low:
        return range_low
  elif num>range_high:
      return range_high

