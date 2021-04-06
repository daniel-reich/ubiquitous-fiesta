
def diving_minigame(lst):
  b_list=[4 if x>=0 else -2 for x in lst]
  start=10
  for x in b_list:
    start+=x
    if start<=0:
      return False
    elif start>10:
      start=10
  return True

