
def track_robot(*steps):
  y = sum(i for i in steps if steps.index(i)%4 == 0) - sum(i for i in steps if steps.index(i)%4 == 2 )
  x = sum(i for i in steps if steps.index(i)%4 == 1) - sum(i for i in steps if steps.index(i)%4 == 3)
  return [x,y]

