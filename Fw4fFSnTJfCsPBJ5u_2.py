
def how_many_missing(lst):
  if len(lst) <2:
    return 0
  return (lst[-1]-lst[0]+1)-len(lst)

