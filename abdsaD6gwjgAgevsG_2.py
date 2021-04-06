
def power_ranger(power, minimum, maximum):
  
  lst = [1,2,3,4,5,6,7,8,9,10]
  a = 0
  counter = 0
  for num in lst:
    a = num ** power
    if (a >= minimum) and (a <= maximum):
      counter += 1
    elif a < minimum:
      continue
    elif a > maximum:
      break
  return counter

