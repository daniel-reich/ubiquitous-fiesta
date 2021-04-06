
def gold_distribution(gold):
  mubashir, matt = 0, 0
  
  while len(gold) != 0:
    if gold[0] >= gold[-1]:
      mubashir += gold.pop(0)
    else:
      mubashir += gold.pop(-1)
      
    if gold[0] >= gold[-1]:
      matt += gold.pop(0)
    else:
      matt += gold.pop(-1)
      
  return [mubashir, matt]

