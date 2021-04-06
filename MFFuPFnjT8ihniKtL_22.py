
def bug_jump(height, time):
  a=height**.5
  time=time/1000
  y=round(height-(time-a)**2,2)
  if y%1==0:
    y=int(y)
  v=-2*(time-a)
  if y>=0:
    if v>0:
      return [y, 'up']
    else:
      return [y, 'down']
  else:
    return [0, None]

