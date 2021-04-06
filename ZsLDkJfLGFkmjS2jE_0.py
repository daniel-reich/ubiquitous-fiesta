
def diving_minigame(lst):
  breath = 10
  
  for i in lst:
    if i < 0:
      breath -= 2
    else:
      breath = min(breath+4, 10)
    
    if breath <= 0: return False
  return True

