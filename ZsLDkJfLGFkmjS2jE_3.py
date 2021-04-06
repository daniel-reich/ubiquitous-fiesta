
def diving_minigame(lst, x = 10):
  for i in lst:
    if i < 0:
      x -= 2
      if x <= 0:
        return False
    else:
      x += 4
      if x > 10:
        x = 10
  return True

