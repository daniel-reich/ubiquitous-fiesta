
def diving_minigame(lst):
  b = 10
  for x in lst:
    b -= 2 if x < 0 else -4 if b < 7 else b - 10
    if b <= 0:
      return False
  return b > 0

