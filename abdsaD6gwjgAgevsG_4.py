
def power_ranger(power, minimum, maximum):
  counter = 0
  for i in range(1,300):
    if i**power>=minimum and i**power<=maximum:
      counter+=1
  return counter

