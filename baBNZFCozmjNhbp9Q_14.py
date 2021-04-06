
def box_seq(step):
  score=0
  for i in range(1,step+1):
      if i%2!=0:
          score+=3
      if i%2==0:
          score-=1
  return score

