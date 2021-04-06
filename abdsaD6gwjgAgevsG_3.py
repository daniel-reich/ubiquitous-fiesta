
def power_ranger(power, minimum, maximum):
  count = 0
  data = range(minimum - 1, maximum + 1)
  for x in range(1, maximum + 1):
    b = x ** power
    if b in data:
      count += 1
  return count

