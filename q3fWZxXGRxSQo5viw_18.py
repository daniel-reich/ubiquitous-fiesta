
def cal(depth):
  time = 1
  dist = 5
  time_mark = 0
  while dist < depth:
    if (time - time_mark) % 30 == 0:
      time += 10
      time_mark = time
      dist -= 30
    time += 1
    dist += 5
  return time

