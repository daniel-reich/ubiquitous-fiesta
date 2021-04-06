
def accumulating_list(lst):
  return list(map(lambda x: sum(lst[:x]),range(1,len(lst)+1)))

