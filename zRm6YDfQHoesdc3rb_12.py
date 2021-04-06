
def rectangles(step):
  total = 0
  for i in range(step,0,-1):
    for j in range(i):
      total += i**2
  return total

