
def power_ranger(power, minimum, maximum):
  values = 0
  i = 1
  while i ** power <= maximum:
    if minimum <= i ** power <= maximum:
      values += 1
    i += 1
  return values

