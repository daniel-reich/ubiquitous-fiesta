
def track_robot(*steps):
  cod = [0,0]
  for i in range(0,len(steps)):
    mod = i % 4
    if mod == 0:
      cod[1] += steps[i]
    elif mod == 1:
      cod[0] += steps[i]
    elif mod == 2:
      cod[1] -= steps[i]
    else:
      cod[0] -= steps[i]
  return cod

