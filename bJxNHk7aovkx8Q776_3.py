
def gold_distribution(gold):
  result = [0, 0]
  mark = 0
  while gold:
    if gold[0] >= gold[-1]:
      add = gold[0]
      gold.pop(0)
    else:
      add = gold[-1]
      gold.pop(-1)
    result[mark] += add
    mark = 0 if mark else 1
  return result

