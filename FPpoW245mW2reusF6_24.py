
def even_last(lst):
  if lst==[]:
    return 0
  return sum(x for i,x in enumerate(lst) if not i%2)*lst[-1]

