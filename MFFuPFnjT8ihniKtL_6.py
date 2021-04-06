
def bug_jump(height, time):
  time = time/1000
  height_return = 0
  direction = "None"
  y = -(time-(height**0.5))**2 + height
  gradient = -2*(time-(height)**0.5)
  if y <=0:
    height_return = 0
    direction = None
  else:
    height_return = round(y,2)
  if gradient >=0 and y > 0:
    direction = "up"
  elif gradient <=0 and y > 0:
    direction = "down"
  return([height_return,direction])

