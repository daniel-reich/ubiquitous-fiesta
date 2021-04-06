
def rectangles(step):
  r=1
  if step == 0:
    return 0
  elif step == 1:
    return 1
  else:
    for i in range(2,step+1):
      r += i
    return r**2

