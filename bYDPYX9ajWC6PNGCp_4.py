
def track_robot(*steps):
  position = [0,0]
  order = [4,3,2,1]
  for step in steps:
    type = order.pop()
    if type == 4:
      position[0] -= step
    elif type == 3:
      position[1] -= step
    elif type == 2:
      position[0] += step
    else:
      position[1] += step
    order.insert(0, type)
  return position

