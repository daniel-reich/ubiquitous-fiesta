
def possible_path(lst):
  poss={'1':'2','2':'1H','H':'24','4':'3H','3':'4'}
  for i in range(len(lst)-1):
    if not str(lst[i+1]) in poss[str(lst[i])]:return False
  return True

