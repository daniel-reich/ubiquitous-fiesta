
def power_ranger(power, minimum, maximum):
  cnt=0
  for num in range(minimum,maximum+1):
    res=num**(1/power)
    if (res).is_integer():
      cnt+=1
  return cnt

