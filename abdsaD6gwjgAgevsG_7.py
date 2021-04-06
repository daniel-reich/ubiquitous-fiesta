
def power_ranger(power, minimum, maximum):
  num = 0
  for i in range(minimum, maximum + 1):
    if i**(1./power) % 1 == 0:
      num+=1
  return num

