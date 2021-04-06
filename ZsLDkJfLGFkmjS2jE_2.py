
def diving_minigame(lst):
  C = 10;
  for i in lst:
    if C <= 0:
      return False;
    if i < 0:
      C-=2;   
    else:
      C+=4;
      if C >= 10:
        C = 10;
  return C>0;

