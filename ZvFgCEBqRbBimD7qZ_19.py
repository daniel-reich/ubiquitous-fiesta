
def bowling(pins):
  ball=0;score=0;frame=1
  while  frame<11:
    if pins[ball]==10 and ball<len(pins)-2:
      score+=pins[ball]+pins[ball+1]+pins[ball+2]
      ball+=1
    elif pins[ball]+pins[ball+1]==10 and ball<len(pins)-2:
      score+=pins[ball]+pins[ball+1]+pins[ball+2]
      ball+=2
    else:
      score+=pins[ball]+pins[ball+1]
      ball+=2
    frame+=1
  return score

