
def accumulating_list(lst):
  return [sum(lst[:i+1]) for i in range(len(lst))]

