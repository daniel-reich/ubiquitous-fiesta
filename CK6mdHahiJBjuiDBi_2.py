
def can_fit(weights, bags):
  bags = [10 for _ in range(bags)]
  while weights:
    fit = False
    cur_item = weights.pop()
    for index, bag in enumerate(bags):
      if cur_item <= bag:
        bags[index] -= cur_item
        fit = True
        break
    if not fit:
      return False
  return True

