
def add_it_up(lst):
  total = lst[0]
  for elem in range(1,len(lst)):
    if type(lst[elem]) == int or type(lst[elem]) == float:
      total = sum([total,lst[elem]])
    elif type(lst[elem]) == list:
      total = sum([total,lst[elem]],[])
    elif type(lst[elem]) == tuple:
      total = sum([total,lst[elem]],())
  return total

