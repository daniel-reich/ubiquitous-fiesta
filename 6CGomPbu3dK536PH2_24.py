
def accumulating_list(lst):
  return [sum(lst[:i]) for i in range(1, len(lst) + 1)]

