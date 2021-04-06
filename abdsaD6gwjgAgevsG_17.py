
def power_ranger(power, minimum, maximum):
  roots = [i ** (1/power) for i in range(minimum, maximum+1) if (i ** (1/power)).is_integer()]
  return len(roots)

