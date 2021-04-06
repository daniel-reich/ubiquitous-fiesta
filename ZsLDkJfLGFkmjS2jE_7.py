
def diving_minigame(lst):
  s = 10
  for i in lst:
    if i < 0: s -= 2
    else: s += 4
    s = min(s, 10)
    if s == 0: return False
  return s > 0

