
def diving_minigame(lst):
  b = 10
  for x in lst:
    if x >= 0:
      b = min(10, b+4)
    else:
      b -= 2
    if b == 0:
      return False
  return True

