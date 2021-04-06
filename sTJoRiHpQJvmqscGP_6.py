
def daily_streak(lst):
  x = 0
  y = 0
  for i in range(0, len(lst)):
    if lst[i] == True:
      y += 1
    else:
      y = 0
    if y > x:
      x = y
  return x

