
def gold_distribution(gold):
  piles = [0,0]
  matt = False
  for i in range(len(gold)):
    if gold[-1]>gold[0]:
      piles[matt]+=gold.pop()
    else:
      piles[matt]+=gold.pop(0)
    matt = not matt
  return piles

