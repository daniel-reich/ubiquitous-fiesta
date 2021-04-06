
def diving_minigame(lst):
  ret = 10
  for i in lst:
    if i>=0:
      if ret+4<=10:
        ret+=4
      else:
        ret=10
    else:
      ret-=2
    if ret<=0:
      return False
  return True

