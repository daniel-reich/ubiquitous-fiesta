
def how_many_missing(lst):
  return lst[-1]-lst[0]-len(lst)+1 if len(lst)>1 else 0

