
def diving_minigame(lst):
  m = 10
  for i in lst:
    if i < 0 and m > 0:
      m -= 2
    elif m <= 0:
      return False
    if i > 0 and m < 10:
      m += 4
  return m > 0

