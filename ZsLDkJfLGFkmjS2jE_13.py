
def diving_minigame(lst):
  bre=10
  for x in lst:
    if x>=0:
      bre+=4
      if bre>10:bre=10
    else:
      bre-=2
      if bre<=0: return False
  return True

