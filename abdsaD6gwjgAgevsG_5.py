
def power_ranger(power, minimum, maximum):
  '''powers = []
  for num in range(minimum, maximum+1):
    if (num ** (1/power)) % 1 == 0:
      powers.append(num)
  return len(powers)'''
  powers = [num for num in range(minimum, maximum+1) if (num**(1/power)) % 1 == 0]
  return len(powers)

