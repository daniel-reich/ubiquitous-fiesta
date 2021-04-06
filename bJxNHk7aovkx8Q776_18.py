
def gold_distribution(gold):
  steps = 1
  Mubashir = 0
  Matt = 0
  
  while len(gold) > 0:
    bigger_gold = 0
    if gold[0] >= gold[-1]:
      bigger_gold = gold.pop(0)
    else:
      bigger_gold = gold.pop(-1)
​
    if steps % 2 == 1:
      Mubashir += bigger_gold
    else:
      Matt += bigger_gold
    steps += 1
  
  return [Mubashir, Matt]

