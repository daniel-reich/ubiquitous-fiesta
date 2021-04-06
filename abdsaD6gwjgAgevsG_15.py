
def power_ranger(power, minimum, maximum):
  num = 1
  a = 0
  while num**power<=maximum:
    ans = num**power
    if ans >= minimum and ans<= maximum:
      a+=1
    num +=1
    
  if a ==0:
    return None
  return a

