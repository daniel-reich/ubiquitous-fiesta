
def power_ranger(power, minimum, maximum):
  x = 0
  for n in range(1,maximum+1):
    result = n**power
    if result >= minimum and result <= maximum:
      x += 1
    if result >= maximum:
      break
  return x

