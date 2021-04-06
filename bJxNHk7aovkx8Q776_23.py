
def gold_distribution(gold):
  mubashir = matt = 0
  is_matt = False
  while len(gold) > 0:
    select = 0
    if len(gold) == 1:
      select = gold[0]
      gold = []
    else:
      left, right = gold[0], gold[-1]
      if left >= right:
        select = left
        gold = gold[1:]
      elif left < right:
        select = right
        gold = gold[:-1]
    if is_matt:
      matt += select
    else:
      mubashir += select
    is_matt = not is_matt
  return [mubashir, matt]

