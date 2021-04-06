
def diving_minigame(lst):
  breath = 10
  for i in lst:
    if i < 0:
      breath -= 2
    else:
      breath = breath + 4 if breath < 6 else 10
    if breath <= 0:
      return False
  return True

