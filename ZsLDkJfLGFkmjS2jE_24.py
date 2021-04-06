
def diving_minigame(lst):
  b=10
  for i in lst:
    if i<0:
      b-=2
    elif b<6:
      b+=4
    else:
      b=10
    if b<=0:
      break
  return bool(b)

