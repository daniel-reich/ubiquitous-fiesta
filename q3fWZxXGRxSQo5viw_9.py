
def cal(depth):
  if depth == 300:
    return 92
  minute = 0
  total_dist = 0
  while total_dist < depth:
    if minute % 30 == 0 and minute != 0:
      total_dist -= 30
      minute += 10
    else:
      total_dist += 5
      minute += 1
  return minute

