
def accumulating_list(lst):
  return  [sum(lst[:x+1]) for x in range(len(lst))]

