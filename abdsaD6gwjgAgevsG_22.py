
def power_ranger(power, minimum, maximum):
  i=1
  count=0
  while i<maximum+1:
    if minimum<= i**power <= maximum: count+=1
    i+=1
  return count

