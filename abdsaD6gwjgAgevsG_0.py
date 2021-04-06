
def power_ranger(power, minimum, maximum):
  return sum(i**(1/power)%1==0 for i in range(minimum,maximum+1))

