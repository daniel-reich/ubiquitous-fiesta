
def dice_score(throw):
  y = 0
  for x in set(throw):
    if throw.count(x) > 2:
      if x == 2:
        y = 200
      if x == 3:
        y = 300
      if x == 4:
        y = 400
      if x == 6:
        y = 600
  for x in sorted(throw):
    if x == 1:
      y += 100
      if throw.count(x) > 2:
        if y == 300:
          y = 1000
    if x == 5:
      y += 50
      if throw.count(x) > 2:
        if y == 150:
          y = 500
  return y

