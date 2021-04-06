
def dice_score(throw):
  score = 0
  thrown = throw
  for x in throw:
    if throw.count(x)==3 and x==1:
      score +=1000
      thrown = thrown.remove(x)
    elif throw.count(x)==3:
      score += x*100
      thrown= thrown.remove(x)
  return score+(throw.count(1)*100)+(throw.count(5)*50)

