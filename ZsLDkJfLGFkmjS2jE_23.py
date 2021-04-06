
def diving_minigame(lst):
  bm = 10
  for x in lst:
    if x < 0:
      bm -= 2
      if bm <= 0:
        return False
    else:
      bm += 4
      if bm > 10:
        bm = 10
  if bm > 0:
    return True
  else:
    return False

