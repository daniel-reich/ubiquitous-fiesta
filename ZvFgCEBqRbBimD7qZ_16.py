
def bowling(pins):
  score=i=0
  for _ in range(10):
    if pins[i]==10:
      score+=10+pins[i+1]+pins[i+2]
      i+=1
    else:
      sc = pins[i]+pins[i+1]
      score+=sc
      if sc==10: score+=pins[i+2]
      i+=2
  return score

