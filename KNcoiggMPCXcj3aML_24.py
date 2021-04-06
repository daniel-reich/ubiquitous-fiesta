
def number_of_days(c):
  travelled = abs(c[0]) + abs(c[1])
  rested = travelled // 5
  if travelled % 5 == 0: rested -= 1
  
  return travelled + rested

