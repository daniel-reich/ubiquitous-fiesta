
def diving_minigame(lst):
  breath_meter = 10
  is_alive = True
  for depth in lst:
    if depth < 0:
      breath_meter -= 2
      if breath_meter == 0:
        is_alive = False
    elif depth >= 0:
      if breath_meter >= 10:
        breath_meter = 10
      else:
        breath_meter += 4
  return is_alive

