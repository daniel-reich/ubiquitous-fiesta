
def bug_jump(height, time):
  a = -1
  b = -height**(1/2)
  c = height
  
  y = a*(time/1000+b)**2+c
  if y < 0:
    return [0, None]
  else:
    y1 = a*((time-1)/1000+b)**2+c
    if y1 < y:
      dir = "up"
    else:
      dir = "down"
  return [round(y,2),dir]

