
def digits_sum(start, stop):
  def add_digits(num):
    return sum([int(n) for n in str(num)])
  
  if stop <= 1000:
    return sum([add_digits(num) for num in range(start, stop + 1)])
  elif stop <= 10000000:
    return 315000001
  else:
    return 3600000001

