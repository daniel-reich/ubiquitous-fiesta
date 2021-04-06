
def diving_minigame(lst):
  b = 10
  for x in lst:
    if x >=0:
      b += 4
    else:
      b-=2
    b = min(b,10)
    if b <= 0:
      return False
  return True

