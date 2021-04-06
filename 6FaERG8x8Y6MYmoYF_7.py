
def dice_score(throw):
  one=throw.count(1)
  two=throw.count(2)
  thr=throw.count(3)
  fou=throw.count(4)
  fiv=throw.count(5)
  six=throw.count(6)
  score=0
  if one>=3:
    score+=1000
    one-=3
  if two>=3: score+=200
  if thr>=3: score+=300
  if fou>=3: score+=400
  if fiv>=3:
    score+=500
    fiv-=3
  if six>=3: score+=600
  score+=100*one
  score+=50*fiv
  return score

