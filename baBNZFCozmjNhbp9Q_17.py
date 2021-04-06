
def box_seq(step):
  box = 0
  if step == 0:
    return 0
  for x in range(1, step+1):
    if x % 2 != 0:
      box += 3
    if x % 2 == 0:
      box -= 1
  return box

