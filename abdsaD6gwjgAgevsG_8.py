
def power_ranger(power, minimum, maximum):
  count=0
  i=0
  while True:
    if minimum<=i**power<=maximum:
      count = count + 1
      i+=1
    elif i**power< minimum:
      i+=1
    else:
      return count

