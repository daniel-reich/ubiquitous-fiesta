
def gold_distribution(gold):
  mubashir_gold = 0
  matt_gold = 0
  while gold:
    mubashir_gold += max(gold[0], gold[-1])
    gold.remove(max(gold[0], gold[-1]))
    matt_gold += max(gold[0], gold[-1])
    gold.remove(max(gold[0], gold[-1]))
  return [mubashir_gold, matt_gold]

