
def accumulating_list(lst):
  return [sum(lst[0:i]) for i in range(1, len(lst)+1)]

