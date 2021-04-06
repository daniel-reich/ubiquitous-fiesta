
def sum_neg(lst):
  if not lst: return []
  return [len(list(filter(lambda x: x > 0, lst))), sum(filter(lambda x: x < 0, lst))]

