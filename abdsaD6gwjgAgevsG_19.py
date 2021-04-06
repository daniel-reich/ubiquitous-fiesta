
def power_ranger(power, minimum, maximum):
  n = 1
  for i in range(1000):
    if n**power >=minimum:
      break
    else:
      n += 1
  counter = 0
  while n**power <= maximum:
    n += 1
    counter += 1
  return counter

