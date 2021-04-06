
def diving_minigame(lst):
  c = 10
  for i in lst:
    if i > 0:
      if c < 10:
        c += 4
      else:
        c += 0
    elif i < 0:
      c -= 2
      if c == 0:
        return False
  return c > 0

