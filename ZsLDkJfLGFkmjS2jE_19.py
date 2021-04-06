
def diving_minigame(lst):
  tar = 10
  arr = [4 if x>0 else 0 if x==0 else -2 for x in lst]
  for i in range(0,len(arr)):
    tar += arr[i]
    if tar>=10:
      tar = 10
    else:
      if tar==0:
        return False
  return True

