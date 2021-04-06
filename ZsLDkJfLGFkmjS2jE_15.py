
def diving_minigame(lst):
  air_level = 10
  for el in lst:
    if el < 0:
      air_level -= 2
    else:
      air_level = 10 if air_level + 4 > 10 else air_level + 4
    if air_level <= 0:
      return False
  return True

