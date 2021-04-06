
def track_robot(*steps):
  result = [0, 0]
  count = 0
  for i in steps:
    count += 1
    if count == 4:
      result[0] -= i
      count = 0
    elif count == 3 :
      result[1] -= i
    elif count == 2:
      result[0] += i
    elif count == 1:
      result[1] += i
  return result

