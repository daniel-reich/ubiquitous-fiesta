
def halve_count(a, b):
  times = 0
  while (a/2) > b:
    times += 1
    a = a / 2
    
  return times

