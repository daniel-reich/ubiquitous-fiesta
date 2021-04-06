
def rectangles(step):
  k = 0
  while step > 0:
    k += pow(step,3)
    step -= 1
  return k

