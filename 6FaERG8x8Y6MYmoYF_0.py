
def dice_score(throw):
  threes = [0,1000,200,300,400,500,600]
  
  tot = 0
  for i in set(throw):
    if throw.count(i) >=3: tot += threes[i]
    if i ==1:
      tot += throw.count(i)%3*100
    if i ==5:
      tot += throw.count(i)%3*50
  
  return tot

