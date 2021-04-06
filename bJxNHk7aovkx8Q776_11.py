
def gold_distribution(gold):
  Mub=0
  Mat=0
  while gold:
    if gold[0]>=gold[-1]:
      Mub+=gold.pop(0)
    else:
      Mub+=gold.pop()
    if gold[0]>=gold[-1]:
      Mat+=gold.pop(0)
    else:
      Mat+=gold.pop()
  return [Mub, Mat]

