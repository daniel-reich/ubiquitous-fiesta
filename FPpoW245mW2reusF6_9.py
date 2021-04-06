
def even_last(lst):
  return sum(x*lst[len(lst)-1] for x in lst[::2])

