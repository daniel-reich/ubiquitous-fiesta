
def diving_minigame(lst):
  B=[10]
  for x in lst:
    if x<0:
      B.append(B[-1]-2)
    else:
      B.append(B[-1]+4 if B[-1]+4<10 else 10)
  return all(x>0 for x in B)

