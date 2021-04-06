
def even_last(lst):
  if not lst:
    return 0
  else:
    evens = lst[0::2]
    return (sum(evens))*lst[-1]

