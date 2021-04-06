
def gold_distribution(gold):
  mu,ma=[0,0]
  while gold:
    mu+=max(gold[0],gold[-1])
    gold.remove(max(gold[0],gold[-1]))
    ma+=max(gold[0],gold[-1])
    gold.remove(max(gold[0],gold[-1]))
  return [mu,ma]

