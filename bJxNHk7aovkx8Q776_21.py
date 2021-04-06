
def gold_distribution(gold):
  Mubashir,Matt,turn=0,0,0
  while gold:
    if gold[0]>=gold[-1]:
      g=gold.pop(0)
    else:
      g=gold.pop()
    if turn%2:
      Matt+=g
    else:
      Mubashir+=g
    turn+=1
  return [Mubashir,Matt]

